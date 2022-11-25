from countriesclass import country
chile = country("Chile","peso chileno","CLP")
usa = country ("Estados Unidos","dolar estadounidense","USD")
usa.print()
chile.print()
chile.newcurrency("dolar estadounidense","USD")
chile.print()
