<?php
session_start();
// Connect to database
require('../../../Database/index.php');
// Get data
$name_product = isset($_GET["name_product"]) ? $_GET["name_product"] : '';
$number_product = isset($_GET["number_product"]) ? $_GET["number_product"] : '';
// data student

require_once __DIR__ . '/../../../lib/pdf/vendor/autoload.php';

$mpdf = new \Mpdf\Mpdf();
$style =
    '
<style>
.container{
    font-family: "Garuda";
}
.container .wrapper{
    font-size: 12pt;
    text-align: center;
}
h3{
  text-align: center;
  font-family: "Garuda";
  }
h4{
  font-family: "Garuda";
}
p{
  font-family: "Garuda";
}
/* วันที่ */
.date{
  position: relative;
  left: 60%;
}
#customers {
    font-family: Arial, Helvetica, sans-serif;
    border-collapse: collapse;
    width: 100%;
    font-family: "Garuda";
  }
  
  #customers td, #customers th {
    border: 1px solid #000;
    padding: 8px;
  }
  
  #customers tr:nth-child(even){background-color: #f2f2f2;}
  
  #customers tr:hover {background-color: #ddd;}
  
  #customers th {
    padding-top: 12px;
    padding-bottom: 12px;
    text-align: center;
    color: #000;
  }

</style>';
$mpdf->WriteHTML($style);

$text = '
<div class = "container">
    <div class="wrapper">
        <p>ใบเสร็จ ที่ยังไม่ได้แต่ง</p>
    </div>
    <div  class="detail">
        <p>
            ชื่อสินค้า: '.$name_product.'
        </p>
        <p>
            จำนวน: '.$number_product.'
        </p>
    </div>
</div>
';

// $mpdf->AddPage();
$mpdf->WriteHTML($text);

$mpdf->Output();
$conn->close();
