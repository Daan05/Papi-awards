In ziekenhuizen in lage inkomstlanden is het niet altijd goed geregeld met het steriliseren van de medische instrumenten, zoals te zien is in het volgend verslag: 

https://gh.bmj.com/content/2/Suppl_4/e000428 

 

Om te helpen met dit probleem willen wij een relatief goedkope manier bouwen om te zorgen dat de medische ingrepen leiden tot een groter succes, doordat er minder grote kans zal zijn op infecties door geïnfecteerde instrumenten. Dit kan breed gebruikt worden door medisch personeel, speciaal in lage-inkomenslanden, om hun medische instrumenten steriel te maken. 

 

Om ervoor te zorgen dat in elk land onze uitvinding te gebruiken is, hebben we de besturing erg makkelijk gemaakt. Je plaatst de instrumenten in een bak, en dan druk je op de knop die alles in werking zet. Het proces verloopt volledig automatisch. De bak met instrumenten komt in een kokendheet water bak te staan met water van 95-98 °C. Met zo'n hoge temperatuur zullen de virussen en bacteriën kapotgaan en wordt het instrument steriel. Hierna, wanneer de instrumenten eruit zijn gehaald, is het klaar voor gebruik. 

Voor onze uitvinding hebben we een overgebleven gordijnrail gebruikt om een karretje te verplaatsen. Deze gordijnrail wordt in de lucht gehouden met een aantal houten latten. We hebben uiteindelijk een driehoeks-constructie gebruikt om de rail steviger vast te zetten, zie hiervoor het filmpje. Aan die gordijnrail hebben we een houten plank bevestigd als karretje. Hier konden we alles aan hangen wat we maar wilden. 

Aan de ene kant van het bouwwerk hebben we alle elektronica geplaatst. Hier ligt de raspberry pi plus alle kabels voor het aansturen van de motoren. Ook het relais voor het verwarmingselement hebben we hier gemonteerd. 

Het verplaatsen van het karretje doen we met een 12Volts motor. Hier hebben we een as aan vastgemaakt die een touwtje opwindt als de motor draait. Met behulp van twee extra relais kunnen we de draairichting omdraaien. Zo kunnen we het karretje twee kanten op bewegen. We hebben deze twee relais op dezelfde GPIO pin van de raspberry pi aangesloten, omdat het belangrijk is dat ze op exact hetzelfde moment schakelen. Anders krijg je kortsluiting. Op het karretje hebben we ook een motor bevestigt zodat die een mandje met de instrumenten omhoog en naar beneden kan doen. Het samenspel van deze motoren zorgt voor een werkende installatie. Zie ook de tekeningen aan het einde van dit deel. 

Voor de communicatie naar de stappenmotor gebruiken we twee lange snoeren. De voeding voor de motor op het karretje halen we uit een powerbank om kabels te besparen. Anders zouden we nog een lange kabel moeten gebruiken. 

In het midden staat een grotere bak met kokend water. Dit water wordt kokend gehouden door een verwarmingselement die aan en uit gezet wordt door een relais. We meten de temperatuur met de bijgeleverde temperatuur sensor. Het is ons nog niet gelukt om de temperatuur sensor werkend te krijgen, maar dit gaan we zo snel mogelijk na deze inzending regelen. Dat gaat ons wel lukken, maar we hadden tijdgebrek. Als de temperatuur lager is dan 95 graden, gaat het element aan, is het hoger dan 98 graden, gaat het element weer uit.
