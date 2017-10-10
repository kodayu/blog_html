#!perl
use strict;
use warnings;
use List::Util;

die ("USAGE:perl random_select.pl whole_peptide.file select.file") unless @ARGV == 2;
open IN,"$ARGV[0]" || die "$!";
open OUT,"> $ARGV[1]" || die "$!";
my $m = 0;
my @data = <IN>;
chomp @data;
foreach my $data(@data){
	my @line = split /\t/,$data;
	if ($line[1] == 1){
		$m++;
		print OUT "$data\n";
	}
}
@data = List::Util::shuffle @data;   #random break the @
my $n = 0;
foreach my $temp(@data){
	my @line = split /\t/,$temp;
	if ($line[1] == -1){
		$n++;
		print OUT "$temp\n";
	}
	if($m == $n){
		last;
	}
	
}