import datetime
import hashlib

class OylamaChain:    
    def __init__(self,onceki_block_hash,islem_list):
        self.onceki_block_hash=onceki_block_hash
        self.islem_list=islem_list

        self.block_veri="-".join(islem_list)+ "-" + onceki_block_hash
        self.block_sifre= hashlib.sha256(self.block_veri.encode()).hexdigest()   
        

 


toplamEvet=[]
toplamHayir=[]
evetdiyen=["evet diyenler:"]
hayirdiyen=["hayir diyenler:"]
technocracy=" "
kisisayisi = int(input("kac kişi: "))
kisicevap=[]
y=kisisayisi
blocks=[]
sonuc_block = {}
tarih = datetime.datetime.now()
hash = "hjasfjhsg"
zincir=[]
kesin_sonuc=[]
while(kisisayisi > 0):
    tckisiad1=input("adini gir: ")
    demos=input("evet veya hayir gir: ") 
    
    if kisisayisi == y:
        if demos=="evet":
            toplamEvet.append(1)
            evetdiyen.append(tckisiad1)
            blocks=OylamaChain(hash,[demos])
            sonuc_block[1] = [blocks.block_sifre]
            print(blocks.block_sifre,datetime.datetime.now())
            zincir.append(blocks.block_sifre)
            print("---------------")
            for p in zincir:
             print(p)
           
           
         
  
        else:
            toplamHayir.append(0) 
            hayirdiyen.append(tckisiad1)
            blocks=OylamaChain(hash,[demos])  
            print(sonuc_block)
            sonuc_block[1] = [blocks.block_sifre]        
            print(blocks.block_sifre, datetime.datetime.now())
            zincir.append(blocks.block_sifre)
            print("---------------")
            for p in zincir:
             print(p)
   
                        

    else:
        if demos=="evet":
            toplamEvet.append(1)
            evetdiyen.append(tckisiad1)
            blocks=OylamaChain(blocks.block_sifre,[demos])
            print(sonuc_block)    
            sonuc_block[1] = [blocks.block_sifre]     
            print(blocks.block_sifre,datetime.datetime.now())  
            zincir.append(blocks.block_sifre)
            print("---------------")
            for p in zincir:
             print(p)
            
        
  
        else:
            toplamHayir.append(0) 
            hayirdiyen.append(tckisiad1)
            blocks=OylamaChain(blocks.block_sifre,[demos])
            print(sonuc_block)
            sonuc_block[1] = [blocks.block_sifre]
            print(blocks.block_sifre,datetime.datetime.now())
            zincir.append(blocks.block_sifre)
            print("---------------")
            for p in zincir:
             print(p)
            
            
        
    
    kisisayisi = kisisayisi - 1    
    kisicevap.append(demos)
    
    
x=0
ilk_block=" "
ikinci_block=" "




print(sonuc_block[1])

print(toplamEvet)

print(evetdiyen)

print(toplamHayir)

print(hayirdiyen)

print(len(toplamEvet),"kisi evet demistir")

print(len(toplamHayir),"kisi hayır demistir")

print("1=evet - 0=hayır")


if len(toplamEvet)>len(toplamHayir):
     print("------------------------------------- ")
     print("yasa onaylandı ")
     technocracy="yasa onaylandı"
   
     

     
else:   
     print("------------------------------------- ") 
     print("yasa onaylanmadı")
     technocracy="yasa onaylanmadı"
     sifreler=list(technocracy)
    


tyrannos=input("ilan et: ")  
if technocracy==tyrannos:
 print("OYLAMA SORUNSUZ ")
  
else:
 
  print("AÇIKLANAN SONUÇ SİSTEMDEKİ SONUÇ İLE UYUŞMADIĞI İÇİN İŞLEM KABUL EDİLEMEZ!")












