# Tatar cyrill-latin converter
This library is intended to convert cyrillic graphic of tatar language into zamanalif version of latin graphic

## Conversion rules for vowels:

- 'А' 'а' converts into 'A' 'a'. Example: азатлык --> azatlıq, агроном --> agronom
- 'Ә' 'ә' converts into 'Ä' 'ä'. Example: әни --> äni
- 'О' 'о' converts into 'O' 'o'. Example: болыт --> bolıt, фото --> foto
- 'Ө' 'ө' converts into 'Ö' 'ö'. Example: төтен --> töten
- 'У' 'у' converts into 'U' 'u'. Example:  уку --> uku
- 'Ү' 'ү' converts into 'Ü' 'ü'. Example:  бүре --> büre
- 'Ы' 'ы' converts into 'I' 'ı' if this is a short sound. Example: ылыс -> ılıs
- 'ы' converts into 'iy' if this is a long sound in loanwords. Example: сыр --> siyr
- 'Э' 'э' converts into 'E' 'e'. Example: эт --> et, электр -> elektr
- 'И' 'и' converts into 'İ' 'i'. Example: китап --> kitap
- 'у' converts into 'w' in the end of the word after 'а' or 'ә'. Example: Җырлау --> Cırlaw

## Conversion rules for consonants:

- 'Б' 'б' converts into 'B' 'b'. Example: бабай --> babay
- 'Җ' 'җ' converts into 'C' 'c'. Example: җир --> cir, җыр --> cır
- 'Ч' 'ч' converts into 'Ç' 'ç'. Example: ачкыч --> açqıç
- 'Д' 'д' converts into 'D' 'D'. Example: давыл --> dawıl
- 'Ф' 'ф' converts into 'F' 'f'. Example: саф --> saf, фонд --> fond
- 'Г' 'г' converts into 'G' 'g' in syllables with front vowels and in loanwords. Example: гөл --> göl,
  гараж --> garaj
- 'Г' 'г' converts into 'Ğ' 'ğ' in syllables with back vowels. Example: гасыр --> ğasır, мәшгүль --> mäşğül
- 'Һ' 'һ' converts into 'H' 'h'. Example: һава --> hawa, шәһәр --> şähär
- 'Ж' 'ж' converts into 'J' 'j'. Example: аждаха --> ajdaha, журнал --> jurnal
- 'Л' 'л' converts into 'L' 'l'. Example: гөлләр --> göllär
- 'М' 'м' converts into 'L' 'l'. Example: малай --> malay, март --> mart
- 'Н' 'н' converts into 'N' 'n'. Example: төн --> tön
- 'Ң' 'ң' converts into 'Ñ' 'ñ'. Example: зәңгәр --> zäñgär
- 'П' 'п' converts into 'P' 'p'. Example: туп --> tup
- 'Р' 'р' converts into 'R' 'r'. Example: рәхәт --> räxät
- 'С' 'с' converts into 'S' 's'. Example: мисал --> misal
- 'Ш' 'ш' converts into 'Ş' 'ş'. Example: буш --> buş, шахмат --> şaxmat
- 'Т' 'т' converts into 'T' 't'. Example: тар --> tar
- 'В' 'в' converts into 'W' 'w'. Example: дәуләт --> däwlät
- 'В' 'в' from russian's loanwords converts into 'V' 'v'. Example: актив --> aktiv, автор --> avtor, автобус --> avtobus
- 'Х' 'х' converts into 'X' 'x'. Example: хат --> xаt, хлор --> xlor
- 'Я' 'я' converts into 'Ya' 'ya' in words with back vowels. Example: ял --> yal, аяк --> ayaq
- 'Я' 'я' converts into 'Yä' 'yä' in words with front vowels. Example: җәя --> сäyä, сәяхәт --> säyäxät
- 'я' converts into 'a' if it comes after 'и' and in words with back vowels. Example: Нияз --> Niaz
- 'я' converts into 'ä' if it comes after 'и' and in words with front vowels. Example: Әкият --> Äkiät
- 'Я' 'я' converts into 'Ya' 'ya' in loanwords there it sound [a]. Example: тягач -> tyagaç
- 'Й' 'й' converts into 'Y' 'y'. Example: йокы --> yokı, ай -> ay, өй --> öy
- 'Ю' 'ю' converts into 'Yu' 'yu' in words with back vowels. Example: юл --> yul
- 'Ю' 'ю' converts into 'Yü' 'yü' in words with front vowels. Example: юкә --> yükä
- 'ю' converts into 'iü' if it comes after 'и'. Example: бию --> biü, кию --> kiü, тию --> tiü
- 'Ю' 'ю' converts into 'Yu' 'yu' in loanwords. Example: меню --> menyu, бюро --> byuro
- 'Ё' 'ё' converts into 'Yo' 'yo' and can occur only in loanwords. Example: шофер --> şofyor
- 'E' 'e' converts into 'Yi' 'yi' in words with back vowels. Example: ел --> yıl
- 'E' 'e' converts into 'Ye' 'ye' in words with front vowels. Example: егет --> yeget
- 'e' converts into 'e' if it comes after 'и'. Example: Нуриев --> Nuriev
- 'З' 'з' converts into 'Z' 'z'. Example: зур --> zur
- 'Щ' 'щ' converts into 'ŞÇ' 'şç' and can occur only in loanwords. Example: борщ --> borşç
- 'Ц' 'ц' converts into 'S' 's' in the beginning of the words, in the end of the words, after consonants and occur only
  in loanwords. Example: цинк --> sink, кварц --> kvars, цирк --> sirk
- 'ц' converts into 'ts' if it comes after vowels, and it occurs only in loanwords. Example: пицца --> pitsa,
  позиция --> positsiä
