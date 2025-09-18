#Criar uma lista de endereços Web (URLs) e imprimir somente os domínios (sem o "www." e "".com").

urls = ["www.chevrolet.com", "www.loveandbravery.com", "www.humanrights.com", "www.godaddy.com", 
        "www.benice.com", "www.oceaneering.com"]
dominios = [url[4:-4] for url in urls]
print("Os domínios extraídos são:", dominios)

urls_br = ["www.fundaffemg.com.br", "www.bb.com.br", "www.projetodesenvolve.com.br", "www.projetotamar.com.br", 
           "www.amigosecreto.com.br"]
dominios_br = [url[4:-7] for url in urls_br]
print("Os domínios '.com.br' extraídos são:", dominios_br)