# biplang 💥

Sadece 5 kelimeyle yazılan minicik bir programlama dili:

**bip · dut · bum · boom · kaboom**

Ciddi bir dil değil, eğlencesine yapıldı. Ama gerçekten çalışıyor: toplama yapabilir, ekrana yazı yazabilir, döngü kurabilir.

## Nasıl çalıştırılır?

Bilgisayarında Python 3 kurulu olmalı. Sonra terminale şunu yaz:

```
python3 main.py examples/hello.bip
```

Ekranda `hi` yazısını görmelisin. 🎉

Kendi programını yazmak için sonu `.bip` ile biten bir dosya oluştur ve aynı şekilde çalıştır.

## Önce şunu hayal et: kutular

biplang'te bilgisayarın hafızasını **yan yana dizilmiş kutular** gibi düşün. Her kutunun içinde bir sayı var ve başta hepsi `0`.

Bir de **ok** var. Ok hep bir kutuyu gösterir. Başta en soldaki kutuyu gösteriyor:

```
 [0] [0] [0] [0] ...
  ↑
```

Yazdığın her kelime ya okun gösterdiği kutudaki sayıyı değiştirir ya da oku sağa sola kaydırır. Hepsi bu kadar!

## Kelimeler

| Yazdığın | Ne olur? |
|---|---|
| `bip` | Kutudaki sayıyı 1 artırır |
| `dut` | Kutudaki sayıyı 1 azaltır |
| `bum` | Oku bir sağdaki kutuya kaydırır |
| `bum bum` | Oku bir soldaki kutuya kaydırır |
| `boom boom` | Kutudaki sayıyı ekrana yazar (ör. `3`) |
| `boom` | Kutudaki sayıyı **harf** olarak yazar (ör. `104` → `h`) |
| `bip bip kaboom` | Senden bir sayı ister ve kutuya koyar |
| `kaboom` | Döngü başlar |
| `kaboom kaboom` | Döngü biter |

### Küçük bir örnek

```
bip bip bip
boom boom
```

Kutuya 3 kere `bip` dedik, kutuda artık `3` var. `boom boom` ile de ekrana yazdırdık. Çıktı: `3`

## Döngü nasıl çalışır?

`kaboom` ile `kaboom kaboom` arasındaki kelimeler **tekrar tekrar** çalışır. Ne zaman durur? Ok `0` olan bir kutuyu gösterdiğinde.

```
bip bip bip
kaboom
  boom boom
  dut
kaboom kaboom
```

Bu program kutuya 3 koyar, sonra yazdırıp 1 azaltarak döner. Çıktı: `321`. Kutu `0` olunca döngü durur.

> Döngünün içindeki bir şeyin kutuyu eninde sonunda `0` yapması lazım. Yoksa döngü sonsuza kadar döner. Durdurmak için `Ctrl + C`'ye bas.

## Yorum yazmak

Bu 5 kelimenin dışındaki **her şey görmezden gelinir**. Yani istediğin yere not alabilirsin:

```
burası kutuya 2 koyuyor
bip bip
```

⚠️ Tek dikkat etmen gereken şey şu: notlarının içinde bu 5 kelimeden birini kullanma, yoksa komut sanılır.

## Kalıplar hakkında küçük bir not

`bum bum`, `boom boom`, `kaboom kaboom` ve `bip bip kaboom` **aynı satırda** yan yana yazılınca tek komut sayılır. Mesela `bum bum` "iki kere sağa git" demek değil, "sola git" demektir.

Ayrı satırlara yazarsan ayrı komut olurlar:

```
bum
bum
```

Bu iki satır, oku 2 kere sağa kaydırır.

## Örnek programlar

`examples` klasörüne bak:

- `hello.bip`: ekrana `hi` yazar
- `sayac.bip`: 5'ten 1'e geri sayar
- `topla.bip`: senden iki sayı ister ve toplar

## Bilmen gerekenler

- Bir kutu en fazla `255` tutabilir. `255`'e bir `bip` daha dersen `0`'a döner (arabanın kilometre sayacı gibi).
- En soldaki kutudan daha sola gidemezsin, hata alırsın.
- Bir şey ters giderse program sana **hangi satırda** sorun olduğunu söyler.
