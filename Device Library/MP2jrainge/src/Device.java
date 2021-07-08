    //MP2, Justin L. Rainge, CIS 340, 1:30-2:45PM
    import java.util.ArrayList;

    public class Device {
	private ArrayList<Device> deviceList;
	private String SKU;
    private String product;
	private boolean status;
	
	



    public Device() {
    	
    deviceList = new ArrayList<Device>();
    	
    }

    public Device(String SKU, String product, boolean status ) {
    	
    
	this.SKU=SKU;
	
	this.status = true;
	this.product = product;
	
    }

    public void setSKU(String SKU) {
    this.SKU = SKU;
    	
    }
    public String getSKU() {
    return SKU;
    }
  
    public void setAvailability(boolean status) {
    	
    this.status = status;
    
    }
    public boolean getAvailability() {
    return status;	
    }
    
    public void setProductName(String product) {
    this.product = product;
    }
    public String getProductName() {
    return product;
    }
  

    
    		
    	
    public void addDevice(Device device) {

		
    deviceList.add(device);
    			
    		

    }
    public ArrayList<Device>getDeviceList(){
    		
    return deviceList;	
    		
    		   
    		  
    }
    	
    public void displayDeviceList() {
        	 
    for(Device d:deviceList ) {
    			
    			
    d.showDeviceList();
        
    }
    }
        		    
    	
    	 
    	
    public void showDeviceList() {
        	 
    System.out.println(SKU + " " +  product + " " +  status);
    	
    }
    
    

    }
