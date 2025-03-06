grep ':' santhali.log.edited.txt | grep -v '>' > dept.words.en-sat_hi.txt;
awk -F: '{print $2}' dept.words.en-sat_hi.txt > dept.words.sat_hi.txt;
indictrans < dept.words.sat_hi.txt -s hin -t eng | awk '{print $1}' > dept.words.sat_en.txt;

playwright
