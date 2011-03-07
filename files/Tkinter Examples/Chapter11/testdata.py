testData = ['KPVD 111151Z 30008KT 10SM FEW150 SCT230 18/11 A3004 RMK AO2 SLP172 T01780106 10178 20144 53020=',
'KPVD 111251Z 30008KT 10SM FEW150 SCT230 21/10 A3006 RMK AO2 SLP177 T02060100=',
'KPVD 120751Z 00000KT 10SM CLR 15/12 A3024 RMK AO2 SLP240 T01500117=',
'KPVD 112051Z 34008KT 300V010 10SM SCT065 26/09 A3009 RMK AO2 SLP190 T02610089 53005=',
'KPVD 111351Z 31011KT 10SM FEW150 SCT250 22/10 A3006 RMK AO2 SLP179 T02220100=',
'KPVD 111451Z 33010G15KT 10SM CLR SCT150 SCT250 23/09 A3007 RMK AO2 SLP183 T02280094 51011=',
'KPVD 111551Z 34009KT 10SM FEW050 SCT150 SCT250 24/09 A3008 RMK AO2 SLP186 T02390094=',
'KPVD 111651Z 32011G15KT 10SM FEW055 SCT150 SCT250 24/10 A3008 RMK AO2 SLP186 T02440100=',
'KPVD 111751Z 33012G15KT 10SM FEW060 SCT150 SCT250 25/10 A3008 RMK AO2 SLP186 T02500100 10250 20178 50003=',
'KPVD 111851Z 32008G16KT 10SM BKN060 26/09 A3008 RMK AO2 SLP186 T02560094=',
'KPVD 111951Z 33008G15KT 10SM SCT065 25/09 A3009 RMK AO2 WSHFT 1917 SLP188 T02500089=',
'KPVD 112051Z 34008KT 300V010 10SM SCT065 26/09 A3009 RMK AO2 SLP190 T02610089 53005=',
'KPVD 112151Z 35010KT 10SM SCT070 25/08 A3011 RMK AO2 SLP194 T02500083=',
'KPVD 112251Z 33010KT 10SM SCT070 24/08 A3012 RMK AO2 SLP200 T02440083=',
'KPVD 112351Z 32006KT 10SM FEW070 23/09 A3015 RMK AO2 SLP210 T02330089 10267 20233 53019=',
'KPVD 120051Z 31005KT 10SM CLR 22/10 A3017 RMK AO2 SLP217 T02220100=',
'KPVD 120151Z 32006KT 10SM CLR 21/10 A3020 RMK AO2 SLP226 T02060100=',
'KPVD 120251Z 30004KT 10SM CLR 20/09 A3021 RMK AO2 SLP229 T02000094 51020=',
'KPVD 120351Z 32005KT 10SM CLR 19/09 A3022 RMK AO2 SLP231 T01890094=',
'KPVD 120451Z 26003KT 10SM CLR 16/10 A3022 RMK AO2 SLP232 T01610100 402670144=',
'KPVD 120551Z 28003KT 10SM CLR 16/11 A3023 RMK AO2 SLP235 T01610111 10233 20156 53005=',
'KPVD 120651Z 29003KT 10SM CLR 15/12 A3023 RMK AO2 SLP237 T01500117=',
'KPVD 120751Z 00000KT 10SM CLR 15/12 A3024 RMK AO2 SLP240 T01500117=',
'KPVD 120851Z 00000KT 10SM CLR 13/11 A3026 RMK AO2 SLP245 T01330111 53009=',
'KPVD 120951Z 00000KT 10SM CLR 14/12 A3028 RMK AO2 SLP253 T01390117=',
'KPVD 121051Z 00000KT 10SM CLR 17/12 A3030 RMK AO2 SLP258 T01670117=',
'KPVD 121151Z 00000KT 10SM FEW250 20/11 A3031 RMK AO2 SLP261 T02000111 10200 20128 51017=',
'KPVD 121251Z 11005KT 10SM FEW250 22/11 A3031 RMK AO2 SLP263 T02220106=',
'KPVD 121351Z 14005KT 10SM FEW250 24/11 A3031 RMK AO2 SLP264 T02390106=',
'KPVD 121451Z VRB05KT 10SM FEW050 25/11 A3031 RMK AO2 SLP263 T02500106 50002=',
'KPVD 121551Z VRB05KT 10SM FEW050 BKN250 26/08 A3030 RMK AO2 SLP261 T02560078=',
'KPVD 121651Z 12005KT 10SM BKN250 27/09 A3029 RMK AO2 SLP258 T02670089=',
'KPVD 121751Z VRB03KT 10SM FEW050 BKN250 27/09 A3028 RMK AO2 SLP254 T02720089 10272 20200 58008=',
'KPVD 121851Z 16013KT 10SM FEW050 OVC200 26/10 A3029 RMK AO2 SLP255 T02610100=',
'KPVD 121951Z 18009KT 10SM FEW110 BKN180 25/09 A3029 RMK AO2 SLP257 T02500094=',
'KPVD 122051Z 18010KT 10SM FEW110 BKN150 24/09 A3030 RMK AO2 SLP258 T02390094 53004=',
'KPVD 122151Z 18007KT 10SM BKN150 23/09 A3029 RMK AO2 SLP256 T02330094=',
'KPVD 122251Z 18005KT 10SM FEW100 BKN140 BKN160 23/10 A3030 RMK AO2 SLP260 VIRGA T02280100=',
'KPVD 122351Z 15005KT 10SM BKN140 BKN160 21/14 A3029 RMK AO2 SLP258 VIRGA T02110144 10267 20211 56000=',
'KPVD 130051Z 16005KT 10SM OVC150 20/14 A3029 RMK AO2 SLP255 T02000139=',
'KPVD 130151Z 16003KT 10SM OVC150 19/14 A3029 RMK AO2 SLP256 T01940139=',
'KPVD 130251Z 00000KT 10SM OVC150 19/15 A3028 RMK AO2 SLP251 T01940150 58007=',
'KPVD 130351Z 00000KT 10SM OVC150 19/15 A3029 RMK AO2 SLP255 T01890150=',
'KPVD 130451Z 00000KT 10SM -RA SCT085 OVC110 19/15 A3028 RMK AO2 RAB45 SLP252 P0000 T01890150 402720128==',
'KPVD 130551Z 00000KT 10SM SCT110 18/16 A3029 RMK AO2 RAE05 SLP255 P0000 60000 T01830161 10211 20183 51004=',
'KPVD 130651Z 04004KT 10SM BKN090 OVC110 18/16 A3027 RMK AO2 SLP248 T01780156=',
'KPVD 130751Z 00000KT 10SM -RA SCT065 BKN120 18/16 A3027 RMK AO2 RAB00E11B29 SLP249 P0000 T01780156==',
'KPVD 130851Z 26003KT 10SM -RA SCT070 OVC110 18/16 A3027 RMK AO2 SLP248 P0000 60000 T01830161 55007==',
'KPVD 130951Z 00000KT 8SM FEW010 BKN100 OVC150 18/17 A3027 RMK AO2 RAE36 SLP249 P0000 T01780167=',
'KPVD 131051Z 06005KT 6SM -RA BR BKN022 OVC110 17/16 A3026 RMK AO2 RAB0953 SLP247 P0000 T01720161=',
'KPVD 131151Z 02006KT 6SM -RA BR BKN022 OVC080 17/16 A3027 RMK AO2 SLP251 P0001 60001 70001 T01670156 10183 20167 58000=']

testData2 = ['KPVD 161951Z 30011KT 9SM FEW070 OVC200 34/17 A3006 RMK AO2 SLP179 T03440167=',
'KPVD 162051Z 21010KT 7SM SCT070 BKN200 33/19 A3006 RMK AO2 SLP177 T03330189 56007=',
'KPVD 162151Z 22010KT 7SM FEW070 SCT140 OVC200 33/19 A3006 RMK AO2 SLP178 T03280189=',
'KPVD 162251Z 25010KT 6SM HZ SCT180 BKN200 31/19 A3007 RMK AO2 SLP180 T03060189=',
'KPVD 162351Z 23007KT 6SM HZ BKN180 BKN200 29/20 A3007 RMK AO2 SLP182 T02890200 10350 20289 53006=',
'KPVD 170051Z 24007KT 6SM HZ BKN180 28/21 A3008 RMK AO2 SLP183 T02780206=',
'KPVD 170151Z 25010KT 6SM HZ CLR 27/21 A3009 RMK AO2 SLP187 T02670206=',
'KPVD 170251Z 24008KT 6SM HZ CLR 26/21 A3008 RMK AO2 SLP187 T02560206 50004=',
'KPVD 170351Z 23007KT 9SM CLR 21/20 A3008 RMK AO2 SLP186 T02500200=',
'KPVD 170451Z 21005KT 10SM CLR 24/19 A3008 RMK AO2 SLP186 T02390189 403500194=',
'KPVD 170651Z 25008KT 10SM FEW085 24/18 A3008 RMK AO2 SLP184 T02390183=',
'KPVD 170751Z 25008KT 9SM CLR 24/18 A3007 RMK AO2 SLP183 T02390183=',
'KPVD 170951Z 26003KT 7SM BKN250 23/18 A3009 RMK AO2 SLP189 T02280183=',
'KPVD 171051Z 26004KT 6SM HZ BKN300 24/19 A3009 RMK AO2 SLP189 T02390189=',
'KPVD 171151Z 29007KT 5SM HZ SCT300 26/20 A3010 RMK AO2 SLP191 HZ ALF T02610200 10261 20228 51005=',
'KPVD 171251Z 27005KT 5SM HZ SCT300 28/21 A3010 RMK AO2 SLP193 HZ ALF T02830206=',
'KPVD 171351Z 29008KT 6SM HZ CLR 31/19 A3009 RMK AO2 SLP189 HZ ALF T03110194=',
'KPVD 171551Z 28012G20KT 6SM HZ CLR 34/18 A3008 RMK AO2 SLP185 HZ ALF T03390183=',
'KPVD 171751Z 28016G19KT 7SM BKN300 35/17 A3005 RMK AO2 SLP175 HZ ALF T03500172 10356 20261 58012=',
'KPVD 171851Z 28016G22KT 7SM BKN300 36/17 A 004 RMK AO2 SLP172 HZ ALF T03610172=',
'KPVD 171951Z 30013KT 6SM HZ FEW180 36/18 A3003 RMK AK2 SLP169 T03610183=',
'KPVD 172051Z 30013KT 6SM HZ SCT180 36/18 A3002 RMK AO2 SLP166 T03560178 58010=',
'KPVD 172151Z 25010KT 6SM HZ FEW100 34/21 A3001 RMK AO2 SLP162 T03390206=',
'KPVD 172251Z 24009KT 6SM HZ FEW100 32/21 A3002 RMK AO2 SLP166 T03220206=',
'KPVD 172351Z 24008KT 5SM HZ FEW100 31/21 A3004 RMK AO2 SLP171 T03060206 10361 20306 53005=',
'KPVD 180051Z 25008KT 5SM HZ CLR 29/21 A3006 RMK AO2 SLP179 T02890206=',
'KPVD 180151Z 25010KT 7SM CLR 28/21 A3008 RMK AO2 SLP185 T02780206=',
'KPVD 180251Z 25010KT 7SM CLR 27/19 A3007 RMK AO2 SLP183 T02720194 50013=',
'KPVD 180351Z 22004KT 10SM CLR 26/19 A3006 RMK AO2 SLP180 T02610189=',
'KPVD 180451Z 22003KT 10SM CLR 26/19 A3006 RMK AO2 SLP178 T02560189 403610228=',
'KPVD 180551Z 22005KT 9SM CLR 24/19 A3005 RMK AO2 SLP176 T02440189 10306 20244 58008=',
'KPVD 180651Z 22005KT 9SM CLR 24/19 A3005 RMK AO2 SLP174 T02390189=',
'KPVD 180751Z 24003KT 9SM CLR 24/19 A3004 RMK AO2 SLP171 T02390189=',
'KPVD 180851Z 00000KT 8SM CLR 24/19 A3004 RMK AO2 SLP173 T02390194 55001=',
'KPVD 180951Z 21004KT 7SM CLR 23/19 A3006 RMK AO2 SLP177 T02330194=',
'KPVD 181051Z 26004KT 4SM HZ CLR 24/19 A3007 RMK AO2 SLP181 T02440194=',
'KPVD 181151Z 24004KT 6SM HZ BKN130 26/20 A3007 RMK AO2 SLP183 T02560200 10256 20233 51010=',
'KPVD 181251Z 30005KT 6SM HZ BKN130 28/21 A3008 RMK AO2 SLP185 T02830211=',
'KPVD 181351Z VRB03KT 5SM HZ SCT130 31/20 A3006 RMK AO2 SLP179 T03060200=',
'KPVD 181451Z 32007KT 6SM HZ SCT200 33/20 A3006 RMK AO2 SLP180 T03280200 58004=',
'KPVD 181551Z 33008KT 7SM SCT200 34/19 A3005 RMK AO2 SLP176 T03390189=',
'KPVD 181651Z 29010KT 6SM HZ FEW200 34/18 A3004 RMK AO2 SLP171 T03440178=',
'KPVD 181751Z 29009KT 8SM FEW200 35/17 A3002 RMK AO2 SLP164 T03500172 10356 20256 58015=',
'KPVD 181851Z 25013G17KT 9SM SCT200 36/16 A3000 RMK AO2 SLP156 T03610156=',
'KPVD 181933Z 29008KT 9SM CLR 36/17 A2998 RMK AO2 WSHFT 1912 HZ ALF=',
'KPVD 181951Z 23009KT 8SM FEW080 36/17 A2998 RMK AO2 WSHFT 1912 SLP151 HZ ALF T03560167=']