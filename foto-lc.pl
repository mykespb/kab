#!/usr/bin/env perl
# myke foto-mk-lc.pl 2011-02-07 1
# make foto file name lowercase 
# repeat for all files in directory
# no dubbing in renaming

print "This is foto-mk-lc.pl 2011-02-07 2015-01-10 2.1 by myke\n\n";

@fa = <*.jpg>;
@fb = <*.JPG>;
%files = ();

foreach $f (@fa) {$files{$f} = 1; }
foreach $f (@fb) {$files{$f} = 1; }

$n = 0;

foreach $f (sort keys %files) {print "$f -> "; 

	$fn = lc $f;
	($name, $ext) = split (/\./, $fn);
#	$name .= '_myke' unless substr($name, -5) eq '_myke';
	$fnew = $name . '.' . $ext;

	print "$fnew\n";

	rename ($f, $fnew) unless $f eq $fnew;
	$n++;

}
# foreach 

print "\nfiles processed: $n\n";
