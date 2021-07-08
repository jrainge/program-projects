    //MP2, Justin L. Rainge, CIS 340, 1:30-2:45PM
    import java.util.ArrayList;
    import java.util.Scanner;

    public class MainSystem {
    static int indexnumber =0;
	static ArrayList<Device> deviceList= new ArrayList<Device>();
	static Scanner scan = new Scanner(System.in);
	static Device deviceSystem = new Device();	
	public static void main(String[] args) {
   
    


	 
	showMenu();
    }
    public static void showProducts() {	
    	
    ArrayList<Device> deviceList;
	deviceList = new ArrayList<Device>();
    String sku1 = "6757A";
	String sku2 = "93P51B";
	String sku3  ="10N8C";
	String sku4 = "85U20";
	String sku5 = "91H2D";
		
	String name1 = "Apple 9.7-inch iPad Pro";
	String name2 = "Amazon Kindle Fire Kids Edition";
	String name3 = "LeapFrog Epic Learning Tablet";
	String name4 = "Amazon Kindle Fire HD 8";
	String name5 = "HP Envy 8 Note";
		
	boolean status1 = true;
	boolean status2 = true;
	boolean status3 = true;
	boolean status4 = false;
	boolean status5 = true;
		
	Device tempDevice1 = new Device(sku1, name1, status1);
	Device tempDevice2 = new Device(sku2, name2, status2);
	Device tempDevice3 = new Device(sku3, name3, status3);
	Device tempDevice4 = new Device(sku4, name4, status4);
	Device tempDevice5 = new Device(sku5, name5, status5);
	    

    deviceList.add(tempDevice1);
    deviceList.add(tempDevice2);
    deviceList.add(tempDevice3);
	deviceList.add(tempDevice4);
    deviceList.add(tempDevice5);
	   
    for(Device d:deviceList ) {
	System.out.println( d.getSKU() + d.getProductName() +  d.getAvailability());
			   
    }
    }
    
	
    public static void showMenu() {
    int answer = 0;
   
     

    do {
    	 
    try {
    	
    System.out.println("1.List Devices by Title" +"\n2.Add New Devices"+ "\n3.Edit Device Information" + "\n4.Search by Device Name" + "\n5.Checkin Device" + "\n6.Checkout Devices" + "\n7.Exit" );

    answer = Integer.parseInt(scan.nextLine());
    
    	 

    switch(answer) {

    case 1:

	showProducts();
	
	for(Device d:deviceList ) {	
    System.out.println( d.getSKU() + d.getProductName()+  d.getAvailability());
	   
    }
    break;

	
    case 2:
	
    addNewProduct();
    break;

    case 3:
    showProducts();
    
    String SKU;
    boolean status = true;
    String product;
    
    System.out.println("Enter product number you want to edt");
    indexnumber = Integer.parseInt(scan.nextLine());
    
    
  


    System.out.println("SKU");
    SKU = scan.nextLine();

    System.out.println("PRODUCT");
    product = scan.nextLine();

	
    Device system = new Device(SKU, product,status);
    deviceList.add(system);
    
    system.getDeviceList().get(indexnumber).setSKU(SKU);
     
    System.out.println("Device Information Changed");
    
    break;
     
    case 4:
    break;

    case 5:
    	 
    for(Device d:deviceList ) {
    			
    showProducts();
    				
    System.out.println("Enter Product Number");
    indexnumber = Integer.parseInt(scan.nextLine());
    				
    				
    if(d.getAvailability()== true) {
    					 
    
    System.out.print( d.getSKU() +  d.getProductName()+  "Available"); 
    }
    else {
    System.out.println(d.getSKU() + d.getProductName()+ "Checked Out"); 
    }
    }
    break;
    

    case 6:
	
    for(Device d:deviceList ) {	
	showProducts();
		
	System.out.println("Enter Product Number");
	indexnumber = Integer.parseInt(scan.nextLine());
		
		
	if(d.getAvailability()== true) {
			 
    indexnumber++;
    System.out.print( d.getSKU() +  d.getProductName()+  "Available"); 
	}
	else {
	System.out.println(d.getSKU() +  d.getProductName()+  "Checked In"); 
	}
	
    break;

    }
    
    answer = 0;
   
    }
    }catch(NumberFormatException e) {
    System.out.println("There was an error. Please try Again");
    }
 
    
    }while(answer!=7);
   
  
    }
     


    public static void addNewProduct() {

   

    String SKU;
    boolean status = true;
    String product;
  


    System.out.println("SKU");
    SKU = scan.nextLine();

    System.out.println("PRODUCT");
    product = scan.nextLine();

	
    Device system = new Device(SKU, product,status);
    deviceList.add(system);



    System.out.println("A new device has been created");
    }

    public static void editInformation() {
	
	
    }

    }
