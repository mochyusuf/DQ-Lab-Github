select kode_produk,nama_produk,harga from ms_produk_1 where harga < 100000
union 
select kode_produk,nama_produk,harga from
ms_produk_2 where harga < 50000