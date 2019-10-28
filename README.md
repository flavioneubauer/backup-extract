### backup-extract

Caso já tenha o adb instalado, pode ignorar o passo 1

1. Baixar android sdk-tools
[https://developer.android.com/studio/releases/platform-tools]

- Extrair o zip e entrar no diretório platform-tools

- testar a conexão com o tablet pelo comando
```bash
adb devices
```

- Verificar:
	- se o modo de transferência de arquivos está ativo
 	- modo desenvolvimento está ativo
 		- depuração usb ativo
 	- também deve aparecer uma tela de autorização que deve ser confirmada

- Quando está ok, após o adb devices, aparece um número hexa e ao lado device no retorno do adb devices

- Agora rodar o comando:
```bash
adb backup -f backup.ab it.murah.cx.app.farmacia
```
- Deve ser autorizado o backup dos dados no device nesse momento

------------------------

2. Extrair os dados
com o arquivo backup.ab em mãos:
2.1. Instalar python 
```bash
sudo apt install python
```

2.2. Converter os dados
```bash
dd if=backup.ab bs=1 skip=24 | python -c "import zlib,sys;sys.stdout.write(zlib.decompress(sys.stdin.read()))" | tar -xvf -
```
- Agora deve ter sido gerado um diretório apps. Dentro dele estão todos os dados abertos para leitura.

2.3. Extrair os dados do banco
```bash
sudo apt install sqlite3
```
Caso já tenha instalado:
```bash
cd apps/it.murah.cx.app.farmacia/db/
sqlite3 -header -csv __cxdb "select * from _ionickv;" > db.csv
```

- Todos os dados do banco agora se encontram no db.csv 
- Cada linha é uma venda, e os dados se encontram no formato json na segunda coluna 
- Cada json possui uma listaImagem, que contém a referência do caminho das imagens

2.4. Converter as imagens
As imagens estão em base64 no diretório apps/it.murah.cx.app.farmacia/f/repo
Criei um pequeno script em python para fazer essa conversão de maneira simples que está no repositório (image-converter.py)
```bash
./image-converter.py
```
