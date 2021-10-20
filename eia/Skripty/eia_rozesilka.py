# coding=UTF-8
import requests
from datetime import datetime, date
import json
import csv

# KNIHOVNA

zamery = [["energetika","Rafinerie ropy nebo primární zpracování ropných produktů."],["energetika","Zařízení ke zplyňování a zkapalňování uhlí a bituminové horniny s kapacitou od stanoveného limitu."],["energetika","Tepelné nebo chemické zpracování uhlí, popřípadě bituminových hornin, včetně výroby uhlíku vysokoteplotní karbonizací uhlí nebo elektrografitu vypalováním nebo grafitizací."],["energetika","Zařízení ke spalování paliv s tepelným výkonem od stanoveného limitu."],["energetika","Průmyslová zařízení k výrobě elektrické energie, páry a teplé vody o výkonu od stanoveného limitu."],["energetika","Vodní elektrárny s celkovým instalovaným elektrickým výkonem od stanoveného limitu."],["energetika","Větrné elektrárny s výškou stožáru od stanoveného limitu."],["energetika","Jaderné elektrárny a jiné jaderné reaktory včetně demontáže nebo konečného uzavření těchto elektráren nebo reaktorů s výjimkou výzkumných zařízení pro výrobu a přeměnu štěpných a množivých látek, jejichž maximální výkon nepřesahuje 1 kW nepřetržitého tepelného výkonu."],["energetika","Zařízení na přepracování vyhořelého jaderného paliva."],["energetika","Zařízení na obohacování nebo výrobu jaderného paliva."],["energetika","Zařízení určená pro zpracování vyhořelého nebo ozářeného jaderného paliva nebo vysoce aktivních radioaktivních odpadů."],["energetika","Zařízení určená pro"],["energetika","Zařízení ke zpracování a skladování radioaktivního odpadu, vrty pro ukládání jaderného odpadu."],["energetika","Hlubinné geotermální vrty a hloubkové vrty pro zásobování vodou u vodovodů s hloubkou od stanoveného limitu."],["energetika","Hlubinné vrty neuvedené v předchozím bodě s výjimkou vrtů pro výzkum stability půdy a s výjimkou vrtů, jejichž realizací nemůže dojít k propojení hydrogeologických horizontů či výraznému ovlivnění hydrogeologických poměrů v území."],["kovy","Integrovaná zařízení pro primární tavbu litiny a oceli."],["kovy","Zařízení k výrobě surového železa nebo oceli (primární nebo sekundární tavení), včetně kontinuálního lití."],["kovy","Zařízení na zpracování železných kovů: slévárny, válcovny za tepla, kovárny a zařízení k nanášení ochranných povlaků z roztavených kovů."],["kovy","Zařízení na výrobu neželezných surových kovů z rudy, koncentrátů nebo druhotných surovin metalurgickými, chemickými nebo elektrolytickými postupy."],["kovy","Zařízení na tavení, včetně slévání slitin, neželezných kovů (kromě vzácných kovů), včetně přetavovaných produktů a provoz sléváren neželezných kovů."],["kovy","Pražení nebo slinování kovové rudy včetně sulfidické rudy."],["kovy","Zařízení pro povrchovou úpravu kovů nebo plastických hmot s použitím elektrolytických nebo chemických postupů s objemem lázní od stanoveného limitu."],["kovy","Zařízení pro povrchovou úpravu látek, předmětů nebo výrobků, používající organická rozpouštědla při spotřebě organických rozpouštědel stejné nebo vyšší než alespoň jeden ze stanovených limitů."],["kovy","Tváření výbuchem."],["kovy","Zařízení k získávání azbestu."],["kovy","Zařízení ke zpracování a přeměně azbestu a výrobků obsahujících azbest pro azbestocementové výrobky s produkcí konečných výrobků od stanoveného limitu."],["kovy","Zařízení ke zpracování a přeměně azbestu a výrobků obsahujících azbest pro třecí materiály s produkcí konečných výrobků od stanoveného limitu."],["kovy","Zařízení ke zpracování a přeměně azbestu a výrobků obsahujících azbest pro další používání azbestu se spotřebou vstupní suroviny od stanoveného limitu."],["kovy","Zařízení na výrobu azbestu a produktů obsahujících azbest."],["kovy","Integrovaná zařízení k průmyslové výrobě základních organických a anorganických chemických látek a směsí chemickou přeměnou (například uhlovodíky, kyseliny, zásady, oxidy, soli, chlór, amoniak)."],["kovy","Integrovaná zařízení k průmyslové výrobě základních přípravků na ochranu rostlin a biocidů chemickou přeměnou."],["kovy","Integrovaná zařízení k průmyslové výrobě fosforečných, dusíkatých a draselných hnojiv chemickou přeměnou."],["kovy","Integrovaná zařízení k průmyslové výrobě základních farmaceutických produktů biologickou nebo chemickou cestou."],["kovy","Výroba chemických látek a směsí a zpracování meziproduktů od stanoveného limitu (například pesticidy a farmaceutické produkty, nátěrové hmoty a peroxidy)."],["kovy","Integrovaná zařízení k průmyslové výrobě výbušin chemickou přeměnou."],["kovy","Zařízení k delaboraci nebo ničení výbušin, munice, střeliva a pyrotechnických předmětů chemickou přeměnou."],["kovy","Zařízení na výrobu cementu, vápna nebo zpracování magnezitu od stanoveného limitu."],["kovy","Zařízení na výrobu skla a skelných vláken s kapacitou tavení od stanoveného limitu."],["kovy","Zařízení k tavení minerálních látek nebo výrobě minerálních vláken s kapacitou od stanoveného limitu."],["kovy","Zařízení k výrobě umělých minerálních vláken s kapacitou od stanoveného limitu."],["kovy","Zařízení na výrobu keramických produktů vypalováním, zejména střešních tašek, cihel, žáruvzdorných cihel, dlaždic, kameniny nebo porcelánu s kapacitou od stanoveného limitu, výroba ostatnich stavebních hmot a výrobků s kapacitou od stanoveného limitu."],["kovy","Výroba nebo zpracování polymerů, elastomerů, syntetických kaučuků nebo výrobků na bázi elastomerů s kapacitou od stanoveného limitu."],["doprava","Letiště se vzletovou a přistávací dráhou s délkou od stanoveného limitu."],["doprava","Celostátní železniční dráhy."],["doprava","Železniční a intermodální zařízení, překladiště a železniční dráhy s délkou od stanoveného limitu."],["doprava","Tramvajové, trolejbusové, nadzemní a podzemní dráhy, visuté dráhy nebo podobné dráhy zvláštního typu sloužící výhradně nebo zvláště k přepravě lidí."],["doprava","Dálnice I. a II. třídy."],["doprava","Silnice nebo místní komunikace o čtyřech a více jízdních pruzích, včetně rozšíření nebo rekonstrukce stávajících silnic nebo místních komunikací o dvou nebo méně jízdních pruzích na silnice nebo místní komunikace o čtyřech a více jízdních pruzích, o souvislé délce od stanoveného limitu."],["doprava","Silnice všech tříd a místní komunikace I. a II. třídy o méně než čtyřech jízdních pruzích od stanovené délky (a), ostatni pozemní komunikace od stanovené délky (a) a od stanovené návrhové intenzity dopravy předpokládané pro novostavby a ročního průměru denních intenzit pro stávající stavby (b)."],["doprava","Vodní cesty, přístavy, přístaviště a překladiště pro plavidla s výtlakem od stanoveného limitu."],["doprava","Přístavy, přístaviště a překladiště pro plavidla s výtlakem od stanoveného limitu."],["doprava","Vodní cesty a úpravy toků sloužící k jejich splavnění, úpravy toků sloužící k ochraně proti povodním, pokud významně mění charakter toku nebo ráz krajiny."],["odpady","Zařízení k odstraňování nebo využívání nebezpečných odpadů spalováním, fyzikálně-chemickou úpravou nebo skládkováním."],["odpady","Zařízení k odstraňování nebo využívání ostatnich odpadů spalováním nebo fyzikálně-chemickou úpravou s kapacitou od stanoveného limitu."],["odpady","Zařízení k odstraňování nebo využívání nebezpečných odpadů s kapacitou od stanoveného limitu."],["odpady","Zařízení k odstraňování nebo využívání ostatnich odpadů s kapacitou od stanoveného limitu."],["odpady","Odkaliště."],["odpady","Zařízení k odstraňování nebo zpracování vedlejších produktů živočišného původu a odpadů živočišného původu."],["voda","Odběr nebo umělé doplňování podzemních vod s objemem čerpané vody od stanoveného limitu."],["voda","Odběr vody a převod vody mezi povodími řek s objemem odebrané nebo převedené vody od stanoveného limitu (vyjma převodu pitné vody vedené potrubím), pokud cílem tohoto převodu je zabránit případnému nedostatku vody."],["voda","Převod vody mezi povodími řek, vyjma převodu pitné vody vedené potrubím, pokud dlouhodobý průměrný průtok v povodí, odkud se voda převádí, přesahuje 2000 mil. m3 za rok a objem převedené vody dosahuje nebo přesahuje stanovenou část dlouhodobého průměrného průtoku v místě, odkud se voda převádí."],["voda","Odběr vody a převod vody mezi povodími řek s objemem odebrané nebo převedené vody od stanoveného limitu (a), nebo pokud objem odebrané nebo převedené vody dosahuje nebo přesahuje stanovenou část (b) Q355 povodí, odkud se voda odebírá nebo převádí."],["voda","Čistírny městských odpadních vod od stanoveného limitu."],["voda","ostatni čistírny odpadních vod, ze kterých jsou vypouštěny odpadní vody, u nichž lze mít důvodně za to, že s ohledem na charakter výroby, při které odpadní vody vznikají, mohou obsahovat alespoň 1 zvlášť nebezpečnou látku16) nebo alespoň 1 prioritní nebezpečnou látku17), s objemem vypouštěných odpadních vod od stanoveného limitu (a) a ostatni čistírny odpadních vod s objemem vypouštěných odpadních vod od stanoveného limitu (b)."],["voda","Vodní nádrže a jiná zařízení určená k akumulaci vody nebo k dlouhodobé retenci vody, pokud objem akumulované vody dosahuje nebo přesahuje stanovený limit."],["energetika","Potrubí k přepravě plynu, ropy a chemických látek a směsí o vnitřním průměru nad 800 mm a o délce od stanoveného limitu. Produktovody k přepravě toků oxidu uhličitého za účelem jeho ukládání do přírodních horninových struktur, včetně připojených kompresních stanic, o vnitřním průměru nad 800 mm a o délce od stanoveného limitu."],["energetika","Potrubí k přepravě plynu, ropy, páry, chemických látek a směsí a vody o vnitřním průměru od 300 mm a o délce od stanoveného limitu."],["zvirata","Zařízení k chovu drůbeže nebo prasat s prostorem pro více než stanovený počet:"],["zvirata","Zařízení k chovu hospodářských zvířat s kapacitou od stanoveného počtu dobytčích jednotek. (1 dobytčí jednotka = 500 kg živé hmotnosti)."],["zvirata","Rybníky určené k chovu ryb s obsádkou při zarybnění od stanoveného limitu počtu váčkových plůdků hlavní ryby - stáří K0 (a), počtu plůdků hlavní ryby - stáří K1 (b) a počtů násady hlavní ryby - stáří K2 (c)."],["ostatni","Průmyslové závody na výrobu buničiny ze dřeva nebo podobných vláknitých materiálů."],["ostatni","Průmyslové závody na výrobu papíru a lepenek od stanoveného limitu."],["ostatni","Předúprava (například praní, bělení, mercerace) nebo barvení textilních vláken či textilií při kapacitě zpracování od stanoveného limitu."],["ostatni","Vydělávání kůže a kožešin při zpracovatelské kapacitě od stanoveného množství hotových výrobků."],["ostatni","Zařízení na výrobu a zpracování celulózy."],["ostatni","Výroba dřevovláknitých, dřevotřískových, pilinových desek nebo překližek a dýh od stanoveného limitu."],["tezba","Těžba ropy v množství od stanoveného limitu (a) a zemního plynu v množství od stanoveného limitu (b)."],["tezba","Povrchová průmyslová zařízení k těžbě uhlí, ropy, zemního plynu a rud, včetně bituminových hornin na ploše od stanoveného limitu."],["tezba","Stanovení dobývacího prostoru a v něm navržená povrchová těžba nerostných surovin na ploše od stanoveného limitu (a) nebo s kapacitou navržené povrchové těžby od stanoveného limitu (b). Povrchová těžba nerostných surovin na ploše od stanoveného limitu (a) nebo s kapacitou od stanoveného limitu (b). Těžba rašeliny od stanoveného limitu (c)."],["tezba","Stanovení dobývacího prostoru a v něm navržená těžba uranu, těžba uranu a úprava uranové rudy."],["tezba","Stanovení dobývacího prostoru a v něm navržená hlubinná těžba, hlubinná těžba."],["tezba","Těžba nerostných surovin z říčního dna."],["tezba","Úprava uhlí (včetně lignitu) s kapacitou od stanoveného limitu."],["energetika","Nadzemní vedení elektrické energie o napětí od 220 kV s délkou od stanoveného limitu."],["energetika","Nadzemní vedení elektrické energie o napětí od 110 kV s délkou od stanoveného limitu."],["kovy","Zařízení ke skladování ropy a ropných produktů od stanoveného limitu a zařízení ke skladování chemických látek a směsí klasifikovaných jako nebezpečné v souladu s nařízením Evropského parlamentu a Rady (ES) č. 1272/2008 o klasifikaci, označování a balení látek a směsí s kapacitou od stanoveného limitu."],["kovy","Skladování zemního plynu a jiných hořlavých plynů s objemem zásobního prostoru od stanoveného limitu."],["kovy","Povrchové skladování fosilních paliv s kapacitou zásobníku od stanoveného limitu."],["kovy","Úložiště oxidu uhličitého18)."],["kovy","Zařízení k zachytávání oxidu uhličitého za účelem jeho ukládání do přírodních horninových struktur18), a to ze zařízení, která vždy podléhají posouzení vlivů záměru na životní prostředí podle tohoto zákona, nebo ze zařízení o celkové roční kapacitě zachyceného oxidu uhličitého 1,5 megatuny nebo vyšší18)."],["kovy","Zařízení k zachytávání oxidu uhličitého za účelem jeho ukládání do přírodních horninových struktur18) ze zařízení, které nepřísluší do kategorie I."],["ostatni","Záměry uvedené v kategorii I určené výhradně nebo převážně k rozvoji a zkoušení nových metod nebo výrobků s předpokládaným provozem nejdéle 2 roky."],["ostatni","Restrukturalizace pozemků v krajině a záměry využití neobdělávané půdy nebo polopřírodních území k intenzivnímu zemědělskému využívání na ploše od stanoveného limitu."],["ostatni","Projekty vodohospodářských úprav pro zemědělství (např. odvodnění, závlahy, protierozní ochrana, lesnicko-technické meliorace) s celkovou plochou úprav od stanoveného limitu."],["ostatni","Zalesnění nelesního pozemku na ploše od stanoveného limitu (a) nebo odlesnění pozemku za účelem změny způsobu využívání půdy na ploše od stanoveného limitu (b)."],["ostatni","Výroba a montáž motorových vozidel, drážních vozidel, lodí, výroba a oprava letadel a výroba železničních zařízení na výrobní ploše od stanoveného limitu."],["ostatni","Výroba rostlinných nebo živočišných olejů nebo tuků s kapacitou od stanoveného limitu."],["ostatni","Balení a konzervování výrobků živočišného a rostlinného původu s kapacitou výrobků od stanoveného limitu."],["ostatni","Zpracování mléka od stanoveného limitu."],["ostatni","Pivovary s kapacitou výroby od stanoveného limitu (a) a sladovny s kapacitou výroby od stanoveného limitu (b) a lihovary nebo pálenice s kapacitou od stanoveného limitu (c)."],["ostatni","Výroba nealkoholických nápojů s kapacitou od stanoveného limitu."],["ostatni","Výroba cukrovinek a sirupů s kapacitou od stanoveného limitu."],["ostatni","Jatka, masokombináty a zařízení na zpracování ryb (včetně výroby rybí moučky a rybích olejů) s kapacitou výrobků od stanoveného limitu."],["ostatni","Výroba škrobu s kapacitou výroby od stanoveného limitu."],["ostatni","Cukrovary s kapacitou zpracované suroviny od stanoveného limitu."],["cestovani","Výstavba skladových komplexů s celkovou zastavěnou plochou od stanoveného limitu."],["cestovani","Průmyslové zóny a záměry rozvoje průmyslových oblastí s rozlohou od stanoveného limitu."],["cestovani","Záměry rozvoje sídel s rozlohou záměru od stanoveného limitu."],["cestovani","Parkoviště nebo garáže s kapacitou od stanoveného limitu parkovacích stání v součtu pro celou stavbu."],["cestovani","Výstavba obchodních komplexů a nákupních středisek s celkovou zastavěnou plochou od stanoveného limitu."],["cestovani","Stálé tratě pro závodění a testování motorových vozidel s délkou od stanoveného limitu."],["kovy","Testovací lavice motorů, turbín nebo reaktorů."],["kovy","Skladování železného šrotu (včetně vrakovišť) od stanoveného limitu."],["cestovani","Sjezdové tratě, lyžařské vleky, lanovky a související zařízení."],["cestovani","Rekreační přístavy pro plavidla s výtlakem od stanoveného limitu (a) nebo pro plavidla v počtu od stanoveného limitu (b)."],["cestovani","Rekreační a sportovní areály vně sídelních oblastí na ploše od stanoveného limitu (a) a ubytovací zařízení vně sídelních oblastí s kapacitou od stanoveného limitu (b)."],["cestovani","Stálé kempy a autokempy s ubytovací kapacitou od stanoveného limitu."],["cestovani","Tematické areály na ploše od stanoveného limitu, krematoria."]]

# FUNKCE

def ziskatOdberatele():
    header = {"Authorization": "Bearer key54k5x3yMgelzSI"}
    r = requests.get('https://api.airtable.com/v0/appNOLtnUURHjZjZm/Odb%C4%9Bratel%C3%A9', headers=header)
    return r.json()

def projitOdberatele(cetnost, buffer):
    seznam = ziskatOdberatele()
    for osoba in seznam["records"]: # Jedeme postupně po jednotlivých lidech v seznamu adresátů
        odeslat = False
        if osoba["fields"]["Periodicita"] == cetnost: # Filtrujeme ty, co jsou přihlášení k denní rozesílce
            email = ""
            for projekt in buffer: # Jedeme po jednotlivých aktualitách v denním bufferu
                pridat = False
                if 'lokalita' in projekt['uvod'] and projekt['uvod']['stav'] != "Záznam založen" and projekt['uvod']['stav'] != "Ukončeno z jiných důvodů" : # Je vůbec projekt zpracovatelný?
                    if shoda_lokalita(projekt['uvod']['lokalita'], osoba["fields"]["Okresy"]) and shoda_typ(zamerTyp(projekt['uvod']['zarazeni']), osoba["fields"]["Typy"]):
                        pridat = True
                        odeslat = True
                if pridat == True:
                        email += projektHtml(projekt); # Přidáme projekt do těla e-mailu k odeslání

            if email and odeslat:
                # Header
                email_final = '<!doctype html><html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"><head> <title></title> <!--[if !mso]><!-- --> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!--<![endif]--> <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"> <meta name="viewport" content="width=device-width,initial-scale=1"> <style type="text/css"> #outlook a { padding: 0 } body { margin: 0; padding: 0; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100% } table, td { border-collapse: collapse; mso-table-lspace: 0; mso-table-rspace: 0 } img { border: 0; height: auto; line-height: 100%; outline: 0; text-decoration: none; -ms-interpolation-mode: bicubic } p { display: block; margin: 13px 0 } </style> <!--[if mso]> <xml> <o:OfficeDocumentSettings> <o:AllowPNG/> <o:PixelsPerInch>96</o:PixelsPerInch> </o:OfficeDocumentSettings> </xml> <![endif]--> <!--[if lte mso 11]> <style type="text/css"> .outlook-group-fix { width:100% !important; } </style> <![endif]--> <!--[if !mso]><!--> <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,500,700" rel="stylesheet" type="text/css"> <link href="https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700" rel="stylesheet" type="text/css"> <link href="https://fonts.googleapis.com/css?family=Cabin:400,700" rel="stylesheet" type="text/css"> <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700" rel="stylesheet" type="text/css"> <style type="text/css"> @import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400,500,700); @import url(https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700); @import url(https://fonts.googleapis.com/css?family=Cabin:400,700); @import url(https://fonts.googleapis.com/css?family=Open+Sans:400,700); </style> <!--<![endif]--> <style type="text/css"> @media only screen and (max-width:480px) { .mj-column-per-100 { width: 100% !important; max-width: 100% } } </style> <style type="text/css"></style> <style type="text/css"> .hide_on_mobile { display: none !important } @media only screen and (min-width:480px) { .hide_on_mobile { display: block !important } } .hide_section_on_mobile { display: none !important } @media only screen and (min-width:480px) { .hide_section_on_mobile { display: table !important } div.hide_section_on_mobile { display: block !important } } .hide_on_desktop { display: block !important } @media only screen and (min-width:480px) { .hide_on_desktop { display: none !important } } .hide_section_on_desktop { display: table !important; width: 100% } @media only screen and (min-width:480px) { .hide_section_on_desktop { display: none !important } } h1, h2, h3, p { margin: 0 } a { text-decoration: none; color: inherit } @media only screen and (max-width:480px) { .mj-column-per-100 { width: 100% !important; max-width: 100% !important } .mj-column-per-100>.mj-column-per-75 { width: 75% !important; max-width: 75% !important } .mj-column-per-100>.mj-column-per-60 { width: 60% !important; max-width: 60% !important } .mj-column-per-100>.mj-column-per-50 { width: 50% !important; max-width: 50% !important } .mj-column-per-100>.mj-column-per-40 { width: 40% !important; max-width: 40% !important } .mj-column-per-100>.mj-column-per-33 { width: 33.333333% !important; max-width: 33.333333% !important } .mj-column-per-100>.mj-column-per-25 { width: 25% !important; max-width: 25% !important } .mj-column-per-100 { width: 100% !important; max-width: 100% !important } .mj-column-per-75 { width: 100% !important; max-width: 100% !important } .mj-column-per-60 { width: 100% !important; max-width: 100% !important } .mj-column-per-50 { width: 100% !important; max-width: 100% !important } .mj-column-per-40 { width: 100% !important; max-width: 100% !important } .mj-column-per-33 { width: 100% !important; max-width: 100% !important } .mj-column-per-25 { width: 100% !important; max-width: 100% !important } } </style></head><body style="background-color:#fff"> <div style="background-color:#fff"> <!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]--> <div style="margin:0 auto;max-width:600px"> <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%"> <tbody> <tr> <td style="direction:ltr;font-size:0;padding:9px 0 9px 0;text-align:center"> <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="vertical-align:top;width:600px;" ><![endif]--> <div class="mj-column-per-100 outlook-group-fix" style="font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%"> <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top" width="100%"> <tr> <td align="left" style="font-size:0;padding:15px 15px 15px 15px;word-break:break-word"> <div style="font-family:Ubuntu,Helvetica,Arial,sans-serif;font-size:11px;line-height:1.5;text-align:left;color:#000">'

                # Úvod
                email_final+='<p>Dobr&yacute; den,</p> <p>&nbsp;</p> <p>děkujeme, že jste se rozhodli využ&iacute;t n&aacute;&scaron; Hl&aacute;sič EIA. Zas&iacute;l&aacute;me V&aacute;m informace o v&scaron;ech posuzovan&yacute;ch z&aacute;měrech, jež odpov&iacute;daj&iacute; krit&eacute;ri&iacute;m, kter&aacute; jste zadali. Dozv&iacute;te se:</p> <ul> <li>z&aacute;kladn&iacute; informace o z&aacute;měru,</li> <li>v jak&eacute; f&aacute;zi se posuzov&aacute;n&iacute; z&aacute;měru nach&aacute;z&iacute;,</li> <li>jak se do procesu můžete zapojit.&nbsp;</li> </ul> <p>Podrobněj&scaron;&iacute; informace o EIA se dočtete v na&scaron;ich manu&aacute;lech <a href="https://frankbold.org/poradna/zivotni-prostredi/zamery-ovlivnujici-zivotni-prostredi/eia/rada/co-je-eia">Co je to EIA</a> a <a href="https://frankbold.org/poradna/zivotni-prostredi/zamery-ovlivnujici-zivotni-prostredi/eia/rada/jak-se-zapojit-do-procesu-eia">Jak se zapojit do procesu EIA</a>.</p>'

                # Obsah
                email_final+=email

                # Patka
                email_final+='<hr /><a href="https://da.frankbold.org/interview?i=docassemble.FrankBold:newsletterEIA.yml&email='+osoba['fields']['E-mail']+'">Změnit preference odběru</a>'
                email_final+='</div> </td> </tr> </table> </div> <!--[if mso | IE]></td></tr></table><![endif]--> </td> </tr> </tbody> </table> </div></body></html>'
                odeslatEmail(osoba["fields"]["E-mail"],email_final)
                email_final = ""
                email = ""

def projektHtml(projekt):
    zprava = "<br /><hr /><br />"
    # Obecné info
    zprava+='<h1>'+projekt['uvod']['nazev']+'</h1>'
    zprava+='<h2>Obecně o z&aacute;měru</h2>'
    zprava+='<ul><li><a href="https://portal.cenia.cz/eiasea/detail/EIA_'+projekt['uvod']['kod']+'">Odkaz na podrobné informace o záměru</a></li>'
    zprava+='<li><strong>Oznamovatel</strong>: <a href="'+projekt['oznameni']['ic']['link']+'">'+projekt['oznameni']['oznamovatel']+'</a></li>' if projekt['oznameni']['ic'] and projekt['oznameni']['oznamovatel'] else '<li>Oznamovatel: <i>Zatím není uveden</i></li>'
    zprava+='<li><strong>&Uacute;řad, kter&yacute; EIA prov&aacute;d&iacute;</strong>: '+projekt['uvod']['urad']+'</li>'
    zprava+='<li><strong>Typ z&aacute;měru</strong>: '+', '.join(zamerSeznam(projekt['uvod']['zarazeni']))+'</li>' if projekt['uvod']['zarazeni'] else '<li>Typ z&aacute;měru: </i>Zatím není uvedeno</i></li>'
    zprava+='<li><strong>Dotčen&eacute; obce/kraje</strong>: '+dotceneObce(projekt['uvod']['lokalita'])+'</li></ul>'

    # Zveřejnění oznámení
    if projekt['uvod']['stav'] == "Oznámení":
        zprava+='<h2>Bylo zveřejněno oznámení záměru</h2>'
        zprava+='<p><img src="https://da.frankbold.org/packagestatic/docassemble.FrankBold/eia_oznameni.png" alt="Schéma procesu EIA" /></p>'
        zprava+='<ul><li>Informace o oznámení záměru: <a href="'+projekt['oznameni']['info'][0]['link']+'">'+projekt['oznameni']['info'][0]['label']+'</a></li>' if projekt['oznameni']['info'] and projekt['oznameni']['info'][0]['link'] and projekt['oznameni']['info'][0]['label'] else '<ul><li>Informace o oznámení záměru: <i>Zatím není zveřejněno</i></li>'
        zprava+='<li>Oznámení záměru: <a href="'+projekt['oznameni']['text'][0]['link']+'">'+projekt['oznameni']['text'][0]['label']+'</a></li></ul>' if projekt['oznameni']['text'] and projekt['oznameni']['text'][0]['link'] and projekt['oznameni']['text'][0]['label'] else '<ul><li>Oznámení záměru: <i>Zatím není zveřejněno</i></li></ul>'
        zprava+='<p>Oznámení obsahuje popis záměru a to, jaké bude dle oznamovatele záměr mít vlivy na životní prostředí a veřejné zdraví.</p>'
        zprava+='<p><strong>K oznámení se můžete vyjádřit do '+projekt['oznameni']['vyjadreniTermin']+'</strong></p>' if projekt['oznameni']['vyjadreniTermin'] else '<p><strong>K oznámení se můžete vyjádřit do 30 dní ode dne, kdy dotčený krajský úřad zveřejnil oznámení na své úřední desce.</strong></p>'
        zprava+='<p>Využijte náš <a href="https://da.frankbold.org/interview?i=docassemble.VzoryPravnichPodani:vyjadreniEIA.yml&idEIA='+projekt['uvod']['kod']+'"><strong>generátor vyjádření k oznámení EIA</strong>.</a></p>'

    # Zjišťovací řízení
    if projekt['uvod']['stav'] == "Závěry zjišťovacího řízení":
        zprava+='<h2>Byl zveřejněn závěr zjišťovacího řízení: Záměr může mít významný vliv na životní prostředí a bude posuzován</h2>'
        zprava+='<p><img src="https://da.frankbold.org/packagestatic/docassemble.FrankBold/eia_zjistovaci.png" alt="Schéma procesu EIA" /></p>'
        zprava+='<ul><li>Informace o závěru zjišťovacího řízení: <a href="'+projekt['zjistovaci rizeni']['info'][0]['link']+'">'+projekt['zjistovaci rizeni']['info'][0]['label']+'</a></li></ul>' if projekt['zjistovaci rizeni']['info'] and projekt['zjistovaci rizeni']['info'][0]['link'] and projekt['zjistovaci rizeni']['info'][0]['label'] else '<ul><li>Informace o závěru zjišťovacího řízení: <i>Zatím není zveřejněno</i></li>'
        zprava+='<li>Závěry zjišťovacího řízení: <a href="'+projekt['zjistovaci rizeni']['zaver'][0]['link']+'">'+projekt['zjistovaci rizeni']['zaver'][0]['label']+'</a></li></ul>' if projekt['zjistovaci rizeni']['zaver'] and projekt['zjistovaci rizeni']['zaver'][0]['link'] and projekt['zjistovaci rizeni']['zaver'][0]['label'] else '<ul><li>Závěry zjišťovacího řízení: <i>Zatím není zveřejněno</i></li></ul>'
        zprava+='<p>V Závěru zjišťovacího řízení se doporučujeme zaměřit na:</p>'
        zprava+='<ul><li>co všechno musí oznamovatel zahrnout do dokumentace,</li>'
        zprava+='<li>shrnutí všech vyjádření, která k oznámení podaly dotčené správní úřady, územní samosprávné celky&nbsp;i veřejnost.</li></ul>'

    # Nepodléhá dalšímu posuzování
    if projekt['uvod']['stav'] == "Nepodléhá dalšímu posuzování":
        zprava+='<h2>Byl zveřejněn závěr zjišťovacího řízení: Záměr nebude podléhat plnému posouzení</h2>'
        zprava+='<p><img src="https://da.frankbold.org/packagestatic/docassemble.FrankBold/eia_nepodleha.png" alt="Schéma procesu EIA" /></p>'
        zprava+='<ul><li>Informace o závěru zjišťovacího řízení: <a href="'+projekt['zjistovaci rizeni']['info'][0]['link']+'">'+projekt['zjistovaci rizeni']['info'][0]['label']+'</a></li>' if projekt['zjistovaci rizeni']['info'] and projekt['zjistovaci rizeni']['info'][0]['link'] and projekt['zjistovaci rizeni']['info'][0]['label'] else '<ul><li>Informace o závěru zjišťovacího řízení: <i>Zatím není zveřejněno</i></li>'
        zprava+='<li>Závěry zjišťovacího řízení: <a href="'+projekt['zjistovaci rizeni']['zaver'][0]['link']+'">'+projekt['zjistovaci rizeni']['zaver'][0]['label']+'</a></li></ul>' if projekt['zjistovaci rizeni']['zaver'] and projekt['zjistovaci rizeni']['zaver'][0]['link'] and projekt['zjistovaci rizeni']['zaver'][0]['label'] else '<ul><li>Závěry zjišťovacího řízení: <i>Zatím není zveřejněno</i></li></ul>'
        zprava+='<p>Proti negativnímu závěru zjišťovacího řízení se mohou do 30 dnů od vyvěšení na úřední desce odvolat spolky, které splňují zákonné podmínky.</p>'
        zprava+='<p>Využít můžete náš <a href="https://da.frankbold.org/interview?i=docassemble.VzoryPravnichPodani%3AodvolaniSpravni.yml"><strong>generátor odvolání</strong></a>.</p>'

    # Dokumentace
    if projekt['uvod']['stav'] == "Dokumentace":
        zprava+='<h2>Byla zveřejněna dokumentace</h2>'
        zprava+='<p><img src="https://da.frankbold.org/packagestatic/docassemble.FrankBold/eia_dokumentace.png" alt="Schéma procesu EIA" /></p>'
        zprava+='<ul><li>Informace k dokumentaci: <a href="'+projekt['dokumentace']['info'][0]['link']+'">'+projekt['dokumentace']['info'][0]['label']+'</a></li>' if projekt['dokumentace']['info'] and projekt['dokumentace']['info'][0]['link'] and projekt['dokumentace']['info'][0]['label'] else '<ul><li>Informace dokumentace: <i>Zatím není zveřejněno</i></li>'
        zprava+='<li>Dokumentace: <a href="'+projekt['dokumentace']['text'][0]['link']+'">'+projekt['dokumentace']['text'][0]['label']+'</a></li></ul>' if projekt['dokumentace']['text'] and projekt['dokumentace']['text'][0]['link'] and projekt['dokumentace']['text'][0]['label'] else '<ul><li>Dokumentace: <i>Zatím není zveřejněno</i></li></ul>'
        zprava+='<p>Dokumentace podrobněji rozpracovává údaje z oznámení o záměru. Autorizovaná osoba v ní podrobně hodnotí vlivy záměru na životní prostředí a veřejné zdraví.</p>'
        zprava+='<p><strong>K dokumentaci se můžete vyjádřit do '+projekt['dokumentace']['vyjadreniTermin']+'.</strong></p>' if projekt['dokumentace']['vyjadreniTermin'] else '<p><strong>K oznámení se můžete vyjádřit do 14 dní o vyvěšená na úřední desce.</strong></p>'
        zprava+='<p>Využijte náš <a href="https://da.frankbold.org/interview?i=docassemble.VzoryPravnichPodani:vyjadreniEIA.yml&idEIA='+projekt['uvod']['kod']+'"><strong>generátor vyjádření k oznámení EIA</strong>.</a></p>'

    # Veřejné projednání
    if projekt['uvod']['stav'] == "Veřejné projednání":
        zprava+='<h2>Chystá se veřejné projednání</h2>'
        zprava+='<p><img src="https://da.frankbold.org/packagestatic/docassemble.FrankBold/eia_projednani.png" alt="Schéma procesu EIA" /></p>'
        zprava+='<ul><li>Informace o místě a času veřejného projednání: <a href="'+projekt['projednani']['info'][0]['link']+'">'+projekt['projednani']['info'][0]['label']+'</a></li></ul>' if projekt['projednani']['info'] and projekt['projednani']['info'][0]['link'] and projekt['projednani']['info'][0]['label'] else '<ul><li>Informace o místě a času veřejného projednání: <i>Zatím není zveřejněno</i></li></ul>'
        zprava+='<p>Veřejného projednání se můžete zúčastnit a vyjádřit svůj názor.</p>'

    # Posudek
    if projekt['uvod']['stav'] == "Posudek":
        zprava+='<h2>Byl zveřejněn posudek</h2>'
        zprava+='<p><img src="https://da.frankbold.org/packagestatic/docassemble.FrankBold/eia_posudek.png" alt="Schéma procesu EIA" /></p>'
        zprava+='<ul><li>Informace k posudku: <a href="'+projekt['posudek']['info'][0]['link']+'">'+projekt['posudek']['info'][0]['label']+'</a></li>' if projekt['posudek']['info'] and projekt['posudek']['info'][0]['link'] and projekt['posudek']['info'][0]['label'] else '<ul><li>Informace o posudku: <i>Zatím není zveřejněno</i></li>'
        zprava+='<li>Posudek: <a href="'+projekt['posudek']['text'][0]['link']+'">'+projekt['posudek']['text'][0]['label']+'</a></li></ul>' if projekt['posudek']['text'] and projekt['posudek']['text'][0]['link'] and projekt['posudek']['text'][0]['label'] else '<ul><li>Posudek: <i>Zatím není zveřejněno</i></li></ul>'
        zprava+='<p>Posudek nezávisle hodnotí správnost a úplnost dokumentace. Najdete v něm také vypořádání vyjádření, která byla podána k dokumentaci.</p>'

    # Stanovisko
    if projekt['uvod']['stav'] == "Stanovisko":
        zprava+='<h2>Bylo zveřejněno závazné stanovisko</h2>'
        zprava+='<p><img src="https://da.frankbold.org/packagestatic/docassemble.FrankBold/eia_stanovisko.png" alt="Schéma procesu EIA" /></p>'
        zprava+='<ul><li>Závazné stanovisko: <a href="'+projekt['stanovisko']['text'][0]['link']+'">'+projekt['stanovisko']['text'][0]['label']+'</a></li></ul>' if projekt['stanovisko']['text'] and projekt['stanovisko']['text'][0]['link'] and projekt['stanovisko']['text'][0]['label'] else '<ul><li>Stanovisko: <i>Zatím není zveřejněno</i></li></ul>'
        zprava+='<p>Závazné stanovisko je výsledkem procesu EIA. Souhlasné stanovisko obsahuje podmínky, které jsou závazné pro navazující správní řízení.</p><br />'
        zprava+='<p>Co dělat, pokud ve stanovisku najdete nesrovnalosti?</p>'
        zprava+='<ul><li>Spolky, které splňují zákonné podmínky ho mohou napadnout v navazujícím řízení.</li></ul>'
        zprava+='<p>Spolek můžete do navazujícího řízení přihlásit za pomoci vzoru <a href="https://frankbold.org/poradna/zivotni-prostredi/zamery-ovlivnujici-zivotni-prostredi/eia/vzor/oznameni-o-ucastenstvi-v-navazujicim-rizeni">Oznámení o účastenství v navazujícím řízení</a> a případně také vzoru <a href="https://frankbold.org/poradna/zivotni-prostredi/zamery-ovlivnujici-zivotni-prostredi/eia/vzor/podpisova-listina-pro-navazujici-rizeni-eia">Podpisová listina pro navazující řízení EIA</a>. Přihlásit se musíte do 30 dní od doby, kdy úřad na své úřední desce zveřejnil, že zahajuje navazující (př. územní) řízení.</p>'
        zprava+='<ul><li>Každý můžete iniciovat přezkum jeho zákonnosti. Využít můžete vzor <a href="https://frankbold.org/poradna/uzemni-planovani/uzemni-planovani/obrana-proti-uzemnimu-planu/vzor/podnet-k-provedeni-prezkumneho-rizeni">Podnět k provedení přezkumného řízení</a>.</li></ul>'
        zprava+='<p>Podrobnosti se dočtete v manuálu <a href="https://frankbold.org/poradna/zivotni-prostredi/zamery-ovlivnujici-zivotni-prostredi/eia/rada/jak-dosahnout-zruseni-stanoviska-eia">Jak dosáhnout zrušení stanoviska EIA</a>.</p>'

    # Prodloužení stanoviska
    if projekt['uvod']['stav'] == "Prodloužení platnosti stanoviska":
        zprava+='<h2>Bylo vydáno prodloužení platnosti závazného stanoviska</h2>'
        zprava+='<p><img src="https://da.frankbold.org/packagestatic/docassemble.FrankBold/eia_stanovisko.png" alt="Schéma procesu EIA" /></p>'
        zprava+='<ul><li>Prodloužení platnosti závazného stanoviska: <a href="'+projekt['stanovisko']['text'][0]['link']+'">'+projekt['stanovisko']['text'][0]['label']+'</a></li></ul>' if projekt['stanovisko']['text'] and projekt['stanovisko']['text'][0]['link'] and projekt['stanovisko']['text'][0]['label'] else '<ul><li>Prodloužení platnosti závazného stanoviska: <i>Zatím není zveřejněno</i></li></ul>'
        zprava+='<p>Závazné stanovisko je výsledkem procesu EIA. Souhlasné stanovisko obsahuje podmínky, které jsou závazné pro navazující správní řízení.</p>'
        zprava+='<p>Co dělat, pokud ve stanovisku najdete nesrovnalosti?</p>'
        zprava+='<ul><li>Spolky, které splňují zákonné podmínky ho mohou napadnout v navazujícím řízení.</li></ul>'
        zprava+='<p>Spolek můžete do navazujícího řízení přihlásit za pomoci vzoru <a href="https://frankbold.org/poradna/zivotni-prostredi/zamery-ovlivnujici-zivotni-prostredi/eia/vzor/oznameni-o-ucastenstvi-v-navazujicim-rizeni">Oznámení o účastenství v navazujícím řízení</a> a případně také vzoru <a href="https://frankbold.org/poradna/zivotni-prostredi/zamery-ovlivnujici-zivotni-prostredi/eia/vzor/podpisova-listina-pro-navazujici-rizeni-eia">Podpisová listina pro navazující řízení EIA</a>. Přihlásit se musíte do 30 dní od doby, kdy úřad na své úřední desce zveřejnil, že zahajuje navazující (př. územní) řízení.</p>'
        zprava+='<ul><li>Každý můžete iniciovat přezkum jeho zákonnosti. Využít můžete vzor <a href="https://frankbold.org/poradna/uzemni-planovani/uzemni-planovani/obrana-proti-uzemnimu-planu/vzor/podnet-k-provedeni-prezkumneho-rizeni">Podnět k provedení přezkumného řízení</a>.</li></ul>'
        zprava+='<p>Podrobnosti se dočtete v manuálu <a href="https://frankbold.org/poradna/zivotni-prostredi/zamery-ovlivnujici-zivotni-prostredi/eia/rada/jak-dosahnout-zruseni-stanoviska-eia">Jak dosáhnout zrušení stanoviska EIA</a>.</p>'


    return zprava
    # Zpracování informací o projektu EIA do HTML podoby mailu.

def zamerTyp(id):
    vystup = []
    for z in id:
        if "/" in z:
            try:
                vystup.append(zamery[int(z.split("/")[1])-1][0])
            except:
                return vystup
    return vystup

def zamerSeznam(id):
    vystup = []
    for z in id:
        if "/" in z:
            try:
                vystup.append(zamery[int(z.split("/")[1])-1][1])
            except:
                return vystup
    return vystup

def dotceneObce(lok):
    obce = []
    for lokal in lok:
        if len(lok) > 5:
            obce.append(lokal['kraj'])
        else:
            obce.append(lokal['obec'])
    return str(', '.join(list(dict.fromkeys(obce))))

def odeslatEmail(email, obsah): # Odeslání těla mailu a adresáta ke zpracování rozesílky do Integromatu.
    data = { "email": email, "obsah": obsah }
    print(email)
    webhook_data = requests.post(INTEGROMAT_WEBHOOK, data=json.dumps(data),headers={'Content-Type': 'application/json'})
    print(webhook_data.text)

def shoda_lokalita(lokalita, odber):
    odber = odber.split(";")
    if 'all' in odber:
        return True
    for polozka in lokalita:
        if polozka['okres'] in odber:
            return True
    return False

def shoda_typ(typy, odber):
    odber = odber.split(";")
    if 'all' in odber:
        return True
    if shoda_list(typy, odber):
            return True
    return False

def shoda_list(list1, list2):
    for x in list1:
        for y in list2:
            if x == y:
                return True
    return False

# APLIKACE

if date.today().weekday() == 0: # V pondělí rozeslat týdenní buffer
    with open('/home/ubuntu/eia/data/eia_data_tydenni.json', encoding='utf-8') as f:
        tydenniBuffer = json.load(f)
    projitOdberatele("tyden", tydenniBuffer)
    with open('/home/ubuntu/eia/data/eia_data_tydenni.json', 'w', encoding='utf-8') as json_file:
        json.dump([], json_file)
elif 1 <= date.today().weekday() <= 5: # V úterý–sobotu rozeslat denní buffer
    with open('/home/ubuntu/eia/data/eia_data_denni.json', encoding='utf-8') as f:
        denniBuffer = json.load(f)
    projitOdberatele("den", denniBuffer)
    with open('/home/ubuntu/eia/data/eia_data_denni.json', 'w', encoding='utf-8') as json_file:
        json.dump([], json_file)
