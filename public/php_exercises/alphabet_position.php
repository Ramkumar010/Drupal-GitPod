<?php
function alphabet_position($name) {
    $result=[];
    $numbers=['a'=>1,'b'=>2,'c'=>3,'d'=>4,'e'=>5,'f'=>6,'g'=>7,'h'=>8,'i'=>9,'j'=>10,'k'=>11,'l'=>12,'m'=>13,'n'=>14,'o'=>15,'p'=>16,'q'=>17,'r'=>18,'s'=>19,'t'=>20,'u'=>21,'v'=>22,'w'=>23,'x'=>24,'y'=>25,'z'=>26];
    $lowercase=strtolower($name);
    $new_string=(str_split($lowercase));
    //print_r ($new_string);
    foreach ($new_string as $str){
        $x= $numbers[$str];
        array_push($result,$x);
    }
    $y= join(" ",$result);
    echo "$y<br>";

}
alphabet_position("The sunset sets at twelve o' clock.");
alphabet_position("ramkumar123");
?>