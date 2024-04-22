declare variable $aceColl := collection('corpus-xml/?select=*.xml');

declare variable $xSpacer := 300;
declare variable $ySpacer := 100;
declare variable $colors := ("red", "green", "blue");

declare variable $speakerCounts :=
  for $speaker in distinct-values($aceColl//@speaker)
  let $count := count($aceColl//@speaker[. = $speaker])
  order by $count descending
  return 
    <speaker count="{$count}">{$speaker}</speaker>;

$speakerCounts[position() <= 5]

