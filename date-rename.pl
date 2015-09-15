#!/usr/bin/env perl

# date-rename.pl myke 2010-10-30 1.2
# rename files to date_time in current directory
# by their date-time

@files1  = <*.jpg>;
@files2  = <*.JPG>;
@files = (@files1, @files2);

foreach $f (sort @files){
print "\n$f: ";

($mtime) =  (stat($f))[9];
print "$mtime, ";
($seconds, $minutes, $hours, $dom, $month, $year, $wday, $yday, $isdst) = 
	localtime($mtime);
$month++;
$year+=1900;

print "\n$seconds, $minutes, $hours, $dom, $month, $year, $wday, $yday, $isdst -- ";

$dt= sprintf("%04d-%02d-%02d_%02d-%02d-%02d", 
	$year, $month, $dom, $hours, $minutes, $seconds);

print "\nto file: $fname: $dt";

next if $dt eq '';
next if -e "${dt}.jpg";
next if $f eq $fname;

rename ($f, "${dt}.jpg");
}


