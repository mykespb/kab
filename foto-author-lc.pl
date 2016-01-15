#!/usr/bin/env perl
# myke foto-author-lc.pl 2016-01-14 1.0
# make foto file name lowercase and add author's name to it
# repeat for all files in directory
# no dubbing in renaming

print "This is foto-author-lc.pl 2016-01-14 1.0 by myke\n\n";

$addname = shift;
exit if $addname eq "";

@fa = <*.jpg>;
@fb = <*.JPG>;
%files = ();

foreach $f (@fa) {$files{$f} = 1; }
foreach $f (@fb) {$files{$f} = 1; }

$n = 0;

foreach $f (sort keys %files) {print "$f -> "; 

	$fn = lc $f;
	($name, $ext) = split (/\./, $fn);
	$name .= '_' . $addname;
	$fnew = $name . '.' . $ext;

	print "$fnew\n";

	rename ($f, $fnew) unless $f eq $fnew;
	$n++;

}
# foreach 

print "\nfiles processed: $n\n";
