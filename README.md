Program hem linux hemde windows sistemlerde çalışmaktadır ve çalıştırma işlemi çok basittir.

"python spider_trap.py" yazmanız yeterlidir.

![3](https://github.com/meisterlos/Spider_Trap/assets/81145753/3f24f3cf-694e-4bbe-8948-de70744b304e)

Program 8000 port üzerinde çalışmaktadır ve web arayüzüne gittiğimizde bizi bu şekilde bir sayfa karşılamaktadır.

![2](https://github.com/meisterlos/Spider_Trap/assets/81145753/5944bcba-d3bb-44e8-8c86-2079dab7ef09)

Sayfa üzerinde bir adet login page sayfası mevcut ve alt kısımda bir kaç tane url bulunmakdatır. Programın çalışma mantığını sayfa üzerinde herhangi bir linke tıkladığınızda size saniyeler içerisinde bir kaç farklı link daha göstermektedir ve bu durum sonsuza kadar devam etmektedir.
Bunu yapmamın en temel sebebi, bir çok web scanner tool'u botlar yardımıyla site içerisindeki tüm dizinleri keşfederler ve daha sonrasında zafiyet taramasına başlar. Yazmış olduğum programda bu dizinler ve linkler sonsuza kadar gitmektedir ve bir çok web scanner aracı zafiyet tarama işlemine başlayamamaktadır.

Örnek olarak wapiti aracı ile zafiyet taraması başlattım ve herhangi bir sonuç dönmemektedir.

![0](https://github.com/meisterlos/Spider_Trap/assets/81145753/b54f3c32-9249-44e9-926e-1455522874ef)

veya wget aracı ile dosyayı indirmeye çalıştığımda sonsuz döngüye girmektedir ve bu tarama bitmemektedir.

![1](https://github.com/meisterlos/Spider_Trap/assets/81145753/e0c29ce8-ce95-437c-ac89-df3a85279871)
