from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors


class Convert():
    
    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon
        
    def format(self):
        x = self.lat[:-1].split("-")
        y = self.lon[:-1].split("-")
        
        degrees = {"lat":x[0],"lon":y[0]}
        minutes = {"lat":x[1],"lon":y[1]}
        seconds = {"lat":x[2],"lon":y[2]}
        direction = {"lat":self.lat[-1],"lon":self.lon[-1]}
        
        return degrees,minutes,seconds,direction
        
    def to_decimal(self):
        
        degrees,minutes,seconds,direction = self.format()
        
        decimal = []
        
        dd = float(degrees["lat"]) + float(minutes["lat"])/60 + float(seconds["lat"])/(60*60);
        if direction["lat"] == 'S':
            dd *= -1
        decimal.append(dd)

        dd = float(degrees["lon"]) + float(minutes["lon"])/60 + float(seconds["lon"])/(60*60);
        if direction["lon"] == 'W':
            dd *= -1
        decimal.append(dd)
            
        return decimal
            
    def __str__(self):
        decimal = self.to_decimal()
        return f"Latitude  {self.lat} : {str(decimal[0])} \nLongitude {self.lon} : {str(decimal[1])}"


def data_prep(image1,image2):
    
    [x_nir,y_nir]=np.where(image1[:,:,0]==0)
    nir = image1[:,:,0].astype(float)
    nir[x_nir,y_nir]=0.0001

    [x,y]=np.where(image2[:,:,0]==0)
    r = image2[:,:,0].astype(float)
    r[x,y]=0.0001
    
    return nir,r

def plot(NDVI):
    
    x_ticks = np.arange(0,3000,step = 400)
    y_ticks = np.arange(0,2000,step = 200)

    cmap0 = matplotlib.colors.LinearSegmentedColormap.from_list("", ["maroon","white","darkgreen"])

    plt.figure(figsize = (10,10))
    plt.subplot()
    plt.imshow(NDVI,cmap = cmap0,vmin=0,vmax=0.15)
    plt.xticks(x_ticks)
    plt.yticks(y_ticks)
    plt.xlabel("X-axis (feet)")
    plt.ylabel("Y-axis (feet)")
    plt.title("NDVI distribution based on FOV")
    plt.colorbar(shrink = 0.5)
    plt.show()
    
def main():
    #lat = input("Enter the latitude you want to convert  (xx-xx-xxN/S) :")
    #lon = input("Enter the longitude you wnat to convert (xx-xx-xxE/W) :")
    
    while True:
        try:
            lat = input("Enter the latitude you want to convert (xx-xx-xxN/S): ")
            if lat[-1] not in ["N", "S"] or "-" not in lat:
                raise ValueError("Invalid latitude input. Please enter a valid input in the format of xx-xx-xxN/S")
        
            lon = input("Enter the longitude you want to convert (xx-xx-xxE/W): ")
            if lon[-1] not in ["E", "W"] or "-" not in lon:
                raise ValueError("Invalid longitude input. Please enter a valid input in the format of xx-xx-xxE/W")
            
            c = Convert(lat,lon)
            print(c,)
            print("")
    
            im = np.array(Image.open("/Users/aashmanrastogi/Desktop/Code_testing_NoIR/NoIRPhoto_TEST.jpg"))
            im2 = np.array(Image.open("/Users/aashmanrastogi/Desktop/Code_testing_NoIR/RGBPhoto_TEST.jpg"))

            print("shape: "+str(im.shape))
            print("")
    
            nir,r = data_prep(im,im2)
            NDVI = (nir-r)/(nir+r)
            plot(NDVI)
        
            break
        
        except ValueError as e:
            print(e)
            continue
        

if __name__ == "__main__":
    main()
