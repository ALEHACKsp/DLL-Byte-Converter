import argparse

parser = argparse.ArgumentParser(description='[R3nzTheCodeGOD] - DLL - Byte dönüştürücü')
parser.add_argument('input', type=str,help='DLL dosyasının adını veya tam yolunu girin.')
parser.add_argument('--out', default='output.txt', type=str, help='Çıktı dosya adı veya tam yolu.')
parser.add_argument('--key', default='\0', type=str, help='Şifreleme anahtarı ascii dizesi.')

args = parser.parse_args()
dll = bytearray(open(args.input, 'rb').read())

with open(args.out, 'w') as output:
    for count, byte in enumerate(dll, 1):
        output.write(f'{byte ^ ord(args.key[(count - 1) % len(args.key)]):#0{4}x},' + ('\n' if not count % 16 else ' '))