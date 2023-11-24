import sklearn
import streamlit as st
import pickle
import pandas as pd

page_bg_img = '''
    <style>
        body {
            background-image: url("hiv_img.png");
            background-size: cover;
        }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

lr = pickle.load(open('lr.pkl','rb'))
df = pd.read_csv("hiv_dataset_deployment.csv")
proteins = ['Q9HBW0', 'P60568', 'P09651', 'Q6Q788', 'P43629', 'P08637', 'A0A1W2PQB1', 'P01730', 'P10145', 'P48061', 'Q15363', 'Q8IZ57', 'Q9HC16', 'P05362', 'O75475', 'Q96EB6', 'P23297', 'Q5T7Y4', 'P43630', 'P01889', 'P13501', 'P40305', 'P40933', 'P21926', 'Q14C87', 'Q86YL7', 'Q15116', 'P42081', 'P10321', 'A0A583ZBW8', 'P61073', 'P16410', 'Q05066', 'P13500', 'P03973', 'P01375', 'Q92945', 'Q9P1U0', 'P18089', 'P04040', 'Q6IB77', 'Q9UH17', 'P01589', 'P42680', 'Q92570', 'Q92570', 'P51681', 'P10147', 'P28482', 'P04271', 'A8MRB1', 'P10451', 'P20309', 'Q14573', 'P54259', 'Q86V38', 'P13591', 'P21796', 'O00585', 'P45381', 'P26717', 'Q15848', 'A8K660', 'O94811', 'P42224', 'Q9C035', 'P07998', 'P03999', 'Q9H4A6', 'Q9GZX7', 'P54725', 'P11473', 'P16278', 'P48681', 'P30048', 'P02545', 'P22301', 'P04085', 'Q10589', 'P67809', 'Q9NR12', 'P17735', 'Q7Z7C8', 'P41597', 'Q14242', 'A0A0C4DFY0', 'Q99731', 'Q8IUR6', 'P01563', 'Q86X60', 'Q99653', 'Q9UHD1', 'P02768', 'Q8TES7', 'P04150', 'Q15125', 'O95433', 'P14778', 'Q14693', 'P20701', 'O60763', 'P08684', 'O60603', 'P01579', 'O60934', 'Q99816', 'Q8TD17', 'Q9H1Y0', 'P35372', 'P29466', 'O75832', 'Q14627', 'Q9NSU2', 'Q14005', 'P37231', 'O43918', 'P06744', 'Q9UPZ9', 'Q12800', 'P60709', 'Q99259', 'A0A0S2Z4D9', 'P25440', 'Q15762', 'P02778', 'P21579', 'Q8N1L9', 'O15439', 'Q9Y3Z3', 'Q9Y2S7', 'Q96AG4', 'P08183', 'P25445', 'P49327', 'P02741', 'Q9Y4B6', 'P14317', 'Q13084', 'P01137', 'Q86UE4', 'P01570', 'P04792', 'P27361', 'Q09028', 'P54849', 'Q96QU6', 'Q9GZX6', 'P05412', 'P13232', 'Q15843', 'P51677', 'P10176', 'Q9NRJ3', 'P04233', 'P04114', 'P32320', 'Q9ULV1', 'P51692', 'P13236', 'Q02790', 'P25942', 'P20592', 'P35579', 'P42771', 'Q8N726', 'O43909', 'Q8TAX7', 'P63279', 'Q9UNS1', 'P42574', 'P12318', 'P43694', 'P01588', 'Q13619', 'P10747', 'P34932', 'O60260', 'P23352', 'P01562', 'P01562', 'P25090', 'P05231', 'Q03181', 'Q16539', 'Q86VB7', 'Q8IU57', 'Q9NRF9', 'P00533', 'P43681', 'O75791', 'P28328', 'Q8N7H5', 'Q9NNX6', 'Q29983', 'Q92887', 'Q9NZH6', 'P17252', 'P11226', 'Q99578', 'P78352', 'P28347', 'O60232', 'Q00653', 'P05154', 'Q8IUH3', 'O14519', 'Q16630', 'Q14116', 'P31749', 'A0A0S2Z3D6', 'P63261', 'P41221', 'P07988', 'P04732', 'P03952', 'P26678', 'P25025', 'Q01826', 'O00421', 'Q9UKK6', 'P43699', 'P43699', 'Q5TYM5', 'Q13309', 'P35247', 'P28906', 'P55040', 'O95373', 'Q8TF42', 'Q13889', 'P09960', 'O00206', 'P55211', 'Q16552', 'Q96LB0', 'Q9UKV8', 'Q32MZ4', 'P22087', 'Q9UJY1', 'P46977', 'Q05823', 'Q1RLL8', 'Q13177', 'Q96LA8', 'P81534', 'P81534', 'P04637', 'P01344', 'Q6UY14', 'Q9Y5L0', 'Q96BD6', 'Q6EBC2', 'P14635', 'Q6PD74', 'B0YJ81', 'Q16665', 'P42229', 'P11413', 'P01112', 'Q9HCE1', 'Q07108', 'Q8TDQ0', 'Q9UBL0', 'Q86TI0', 'P05107', 'Q9Y4W2', 'O94992', 'P08133', 'P08581', 'Q9NWH9', 'P15151', 'P62937', 'Q9BQ51', 'Q9NQB0', 'P60880', 'O60930', 'P13489', 'Q6RSH7', 'Q5T4W7', 'Q00987', 'P09326', 'Q86XR7', 'D3DTF8', 'P63241', 'O75369', 'Q96I51', 'P17693', 'P23528', 'Q93034', 'O00501', 'Q14686', 'Q9NZQ3', 'P80098', 'O95365', 'Q9UII4', 'P55273', 'Q8WXG1', 'P35658', 'Q08380', 'P55290', 'P01920', 'Q9Y2C9', 'Q9NZ43', 'Q9H3S7', 'P43004', 'O00182', 'P05771', 'P26599', 'P49767', 'Q13451', 'P24001', 'C6GKH1', 'P09429', 'P11532', 'P09382', 'Q12967', 'P01282', 'P35637', 'Q13324', 'Q96FA3', 'P02649', 'Q9Y458', 'Q9UQC2', 'P10144', 'P18510', 'Q14954', 'B4DJ51', 'Q96HY3', 'Q8N4G2', 'P25106', 'P09874', 'P01270', 'Q9NR97', 'Q96E93', 'Q9UHD0', 'P43627', 'Q15054', 'Q9UBU9', 'Q9UIQ6', 'Q9NRW3', 'P78423', 'Q9UBF6', 'P07996', 'P01106', 'Q14901', 'Q7Z417', 'P50750', 'P78556', 'Q9H2X3', 'P46108', 'O43159', 'P42772', 'Q8NBP7', 'Q8NEV9', 'Q53HV7', 'Q92854', 'Q13224', 'P09601', 'Q96DI8', 'Q9NZQ7', 'P16619', 'P16619', 'Q13469', 'Q14511', 'Q9P2Y5', 'Q13155', 'O15519', 'Q9Y2P5', 'Q04206', 'Q96CP1', 'O00233', 'Q14643', 'Q9NV58', 'P98160', 'Q02246', 'Q92581', 'P02689', 'P11245', 'Q6N069', 'Q9H2H9', 'P01241', 'O00459', 'P19338', 'Q07325', 'P02656', 'P43632', 'Q04323', 'P16284', 'P04179', 'O60264', 'P20333', 'P00797', 'Q693B1', 'O15162', 'Q8WVK1', 'P10415', 'P20815', 'P02766', 'Q8TE12', 'P16871', 'Q16531', 'P40763', 'P24821', 'P01024', 'P05067', 'P13051', 'P02686', 'P13727', 'P00740', 'P0DP23', 'P00742', 'Q9BQ89', 'Q969K3', 'Q9Y5S9', 'Q9BUP3', 'P48506', 'P61769', 'Q8NEN9', 'P23443', 'P11215', 'P14151', 'O00255', 'P07148', 'P12314', 'Q9NP81', 'P25100', 'P35348', 'P04141', 'O00300', 'P53999', 'Q9NQ94', 'Q96GD0', 'P48023', 'P02647', 'A1L3X4', 'Q9NPF7', 'P05019', 'P28329', 'P14784', 'P43403', 'Q9BY32', 'P05112', 'Q16655', 'P08603', 'Q9ULA0', 'P40189', 'P19525', 'Q9H4A3', 'Q03060', 'P49792', 'Q9P2W7', 'P01189', 'P26842', 'P27986', 'P33993', 'Q9UN37', 'O60235', 'P15036', 'P49238', 'Q9H3D4', 'Q13164', 'Q8IYM9', 'P54829', 'P25054', 'Q969V5', 'P20023', 'P48556', 'P50402', 'P35228', 'P60321', 'Q96RN1', 'Q15399', 'P13726', 'P31785', 'Q14943', 'P29074', 'P08253', 'P03372', 'O00522', 'P68363', 'Q14739', 'O76090', 'P55957', 'Q8N7E2', 'Q9ULW0', 'O15455', 'Q8TDS5', 'P01009', 'O15529', 'Q01094', 'P08571', 'Q9UBY5', 'P02812', 'Q13547', 'P60953', 'Q6GTX8', 'P27487', 'P16070', 'P08247', 'P17948', 'P12273', 'Q9Y275', 'O60675', 'Q86WV6', 'P20963', 'O60869', 'P11836', 'P18428', 'Q96C74', 'O15118', 'P10599', 'P15941', 'O14980', 'P19438', 'Q9Y6K5', 'P00488', 'P12104', 'Q16584', 'P24941', 'P43489', 'Q96DA2', 'P27918', 'A0A0S2Z515', 'P14136', 'Q8IUX4', 'P49137', 'P49366', 'P53539', 'Q06520', 'Q495A1', 'Q01523', 'P42768', 'Q8WUM4', 'P02786', 'Q9NZ71', 'P45984', 'Q8N157', 'P60484', 'P28300', 'P49591', 'P42345', 'Q9NQX0', 'P68871', 'Q13526', 'P31391', 'Q7Z6L0', 'P0DMM9', 'Q14653', 'P15813', 'Q9BZW4', 'P07355', 'P01583', 'Q9BZL4', 'P14222', 'Q9HBE4', 'Q14289', 'Q15020', 'P15529', 'P61626', 'Q9BX66', 'P01574', 'P29323', 'P41159', 'P16220', 'O15524', 'P40967', 'Q06124', 'Q15633', 'O43524', 'Q01518', 'Q01638', 'Q9UBP5', 'P18754', 'P63146', 'Q96HW7', 'Q9BY43', 'Q96P20', 'Q9UNQ0', 'Q53H80', 'P14780', 'P17535', 'P27695', 'P21333', 'Q99523', 'Q6P1N0', 'Q99836', 'Q12918', 'P11137', 'Q9BQQ3', 'P00403', 'P35354', 'A5D8V6', 'Q03135', 'Q9UKA9', 'P19838', 'O95057', 'P09543', 'Q12774', 'P00973', 'Q15109', 'P13747', 'P38936', 'O43490', 'Q30201', 'P09038', 'Q14155', 'Q8N8S7', 'Q9NZR4', 'Q70E73', 'P62841', 'O60885', 'P15882', 'P09086', 'Q08AH1', 'O76036', 'P35414', 'Q05516', 'P10071', 'Q13203', 'P22415', 'P29475', 'Q8WY41', 'P25963', 'Q9NYL2', 'P49961', 'P62258', 'Q92574', 'Q86WV8', 'Q01628', 'P06850', 'Q9H6R4', 'P23560', 'P15923', 'Q9Y286', 'P32970', 'O75955', 'P41440', 'Q6P1J6', 'P61457', 'P28065', 'O14791', 'Q01850', 'Q00266', 'P35968', 'P32302', 'P35900', 'Q8TDQ1', 'Q9BVK6', 'P09758', 'P26927', 'Q13043', 'Q9UHD2', 'Q12824', 'P60033', 'Q9H1I8', 'Q9UKV3', 'Q9C0K0', 'P30536', 'Q9BZS1', 'Q9BXR0', 'O75469', 'Q9H3H1', 'P43628', 'P06734', 'P51570', 'Q16625', 'Q9H832', 'Q8NHW4', 'Q8NHW4', 'P17275', 'Q9H2V7', 'Q9Y657', 'O14543', 'P00540', 'P13073', 'P46091', 'P15056', 'P32241', 'P25092', 'P49675', 'Q9ULV5', 'Q96D42', 'Q86Y37', 'Q06455', 'P01100', 'O43281', 'P31995', 'Q6TDU7', 'Q76LX8', 'P51679', 'Q9ULM6', 'Q8TDV0', 'P14679', 'Q14457', 'P17676', 'P80188', 'P35610', 'P49815', 'Q16082', 'P14618', 'P25101', 'Q99714', 'O14625', 'Q15078', 'Q07011', 'Q9NZM5', 'P07900', 'P35916', 'Q9NSE2', 'P55774', 'P41235', 'Q96KG9', 'P02788', 'P42773', 'Q6IAA8', 'P60174', 'P08962', 'P06746', 'P46013', 'P49790', 'P49682', 'Q9NZD1', 'Q9NPP4', 'Q07869', 'P30301', 'Q14392', 'P16435', 'Q99626', 'P51671', 'O75914', 'Q969M7', 'Q96T58', 'Q5VWK5', 'P00747', 'P35225', 'P14174', 'Q9UGN4', 'Q9NSA1', 'P00441', 'Q07666', 'O60936', 'Q7LC44', 'Q9UJ71', 'P03951', 'P52948', 'P08519', 'P22749', 'Q96BK5', 'O75973', 'P05113', 'Q496F6', 'P10912', 'P56817', 'P07339', 'P32246', 'P14859', 'Q96KQ4', 'Q13045', 'Q8TF71', 'A1E959', 'P02753', 'P01130', 'Q03518', 'P31751', 'Q9BUR4', 'P06239', 'Q08999', 'O43324', 'Q13530', 'P05230', 'P30622', 'P57739', 'P01116', 'Q01543', 'P01127', 'P32856', 'Q10981', 'O15245', 'Q13241', 'P31994', 'P56703', 'Q86YT6', 'O60563', 'Q6UW56', 'Q14994', 'P08575', 'P14921', 'Q9UBI1', 'Q7KZF4', 'Q9UBP4', 'Q12959', 'P22314', 'A0A0C4DFY5', 'P41182', 'P06702', 'P48637', 'P32942', 'P51946', 'O43439', 'Q9Y4K3', 'P52757', 'Q9UHI8', 'Q9UBN7', 'P51449', 'P21854', 'P54578', 'P46527', 'P49841', 'Q9UBT2', 'P51861', 'P10070', 'O60333', 'Q96C55', 'Q14677', 'Q96A83', 'A1KXE4', 'P57075', 'Q5T619', 'Q14D33', 'Q6GQQ9', 'Q5T4B2', 'Q86VF2', 'Q8WYH8', 'P26368', 'P04259', 'Q9NP66', 'Q8IYI8', 'Q86XF7', 'Q8NDP4', 'Q96M91', 'O95563', 'Q68DK2', 'Q9NUW8', 'Q8IVW4', 'A6NJ78', 'P19237', 'Q9NS73', 'Q9NR21', 'P43115', 'O43679', 'Q5SQQ9', 'Q8TCT0', 'Q9BSK4', 'Q15696', 'Q9BPU9', 'Q99728', 'P42568', 'Q9UDX3', 'Q66PJ3', 'Q9P1Z0', 'Q9UI95', 'Q9NP70', 'Q9BRP7', 'Q8WTR4', 'P78333', 'Q9BS16', 'Q8WVX9', 'Q9Y2V2', 'Q9NYW8', 'A6NJB7', 'P18075', 'Q8WXB1', 'Q8WTS1', 'Q9NRE2', 'P62380', 'Q5M9N0', 'O95865', 'Q96S52', 'Q99958', 'O43247', 'Q5H9J7', 'Q15051', 'P09603', 'Q9NQ48', 'Q96PC2', 'Q9UEG4', 'O43474', 'Q8WVZ9', 'Q96C12', 'Q8WU79', 'P18206', 'Q14CX5', 'Q14773', 'Q9NVM1', 'Q9NWS6', 'Q32M78', 'Q92989', 'P19784', 'Q9NWX6', 'Q9NU63', 'Q8TC20', 'Q6ZMU5', 'Q13835', 'O15197', 'Q8N4U5', 'Q16600', 'Q9H4F8', 'A1A580', 'Q9UHL9', 'Q86UD0', 'Q9UN30', 'A1L162', 'O60729', 'Q96MT3', 'P20340', 'P52737', 'Q9HD47', 'Q86WR0', 'Q9NP73', 'P51504', 'P06576', 'Q9Y592', 'Q712K3', 'Q9BV68', 'A0A0B4J2F2', 'Q9UHV2', 'Q8IZW8', 'P31350', 'Q9HB20', 'P0DI81', 'P62854', 'Q12798', 'Q16548', 'Q8IU80', 'P17036', 'Q4VC39', 'Q96CN4', 'Q14195', 'Q9HD20', 'P07315', 'P01185', 'P33778', 'Q9NR11', 'O75056', 'O14917', 'Q8NBE8', 'P22304', 'Q06323', 'O95696', 'Q96Q83', 'Q9HAZ1', 'Q6UXG2', 'Q5T447', 'O00755', 'Q16621', 'P57771', 'Q9NUY8', 'P27987', 'Q96C28', 'P62306', 'Q99909', 'Q99743', 'O95864', 'Q7RTY0', 'O76082', 'P62875', 'Q92753', 'Q86WB7', 'Q96BD5', 'Q8N743', 'Q9UII5', 'Q86WW8', 'Q9NRZ7', 'Q8NA72', 'Q9UL15', 'Q9BT40', 'O14764', 'O15130', 'P53677', 'P07101', 'O15084', 'Q9P2B4', 'Q5T7B8', 'Q8WYQ4', 'Q9UI36', 'P62995', 'Q5TEC3', 'Q96DN0', 'Q96DV4', 'O43278', 'O75920', 'P18859', 'Q8IXH7', 'Q14154', 'P28074', 'P48039', 'O43815', 'P48739', 'O75425', 'Q92609', 'P26885', 'Q5T9C2', 'Q01968', 'Q9H0C2', 'O43617', 'P35575', 'Q9P289', 'P62699', 'Q8IV56', 'Q12446', 'P42830', 'Q66K41', 'Q3MII6', 'P40939', 'P55008', 'Q9H310', 'Q499Z4', 'P20336', 'Q96FE7', 'Q9HAV0', 'Q9UHC1', 'Q6XQN6', 'Q9Y217', 'Q96G97', 'Q9H313', 'P53634', 'Q86XR2', 'Q9XRX5', 'Q8WVE6', 'P04155', 'Q7Z6K5', 'Q6PI48', 'Q9BX40', 'P35998', 'Q8NA57', 'Q15326', 'Q6ZQX7', 'P01160', 'Q9UPY6', 'Q9NW81', 'Q8NFH4', 'P84243', 'O00743', 'A2RRD8', 'Q8N6M8', 'Q9Y2I6', 'Q6PCT2', 'O15525', 'Q6PEY1', 'A0JP26', 'P39019', 'P46948', 'P59998', 'P20839', 'Q9NWS8', 'P29274', 'Q8NEY8', 'Q9BRL6', 'P78368', 'O15315', 'P63316', 'Q9H875', 'P51523', 'P0CW24', 'O75146', 'P46087', 'A7E2Y1', 'Q9NW75', 'Q9Y6W5', 'Q8N3Y7', 'Q9Y2X9', 'Q96K58', 'P0CI25', 'P03466', 'P52789', 'O94933', 'Q9BQ75', 'O15403', 'Q14678', 'P17020', 'Q53FE4', 'Q96RD9', 'Q9P1Y5', 'Q96BY6', 'Q99627', 'Q8NCG7', 'O43920', 'P67936', 'Q5JXX7', 'O15550', 'Q96SZ4', 'O95340', 'Q3SY52', 'Q3KNV8', 'Q9H3Q1', 'P35080', 'O15040', 'Q7Z3Z2', 'Q6P1M9', 'Q01853', 'P54278', 'P70288', 'O75616', 'Q96JC1', 'P52298', 'Q9BXI9', 'Q30KQ5', 'Q9UPX6', 'Q96KE9', 'O43390', 'Q14764', 'Q8N0X2', 'Q96M83', 'Q8WVM8', 'Q8IV16', 'P61353', 'O95396', 'P58062', 'Q9NR22', 'A8MVS5', 'Q6PRD1', 'O43808', 'Q96GU1', 'P0A910', 'P58004', 'Q00597', 'Q9UGP8', 'Q9NYQ3', 'Q96DT6', 'P54750', 'P23610', 'Q96M34', 'Q6T310', 'P29846', 'P46439', 'Q8TAP9', 'Q9UNY4', 'Q5JR12', 'Q9BXJ0', 'Q9UNH6', 'O15119', 'Q6UXB8', 'Q9Y478', 'O15266', 'P26640', 'Q587J8', 'Q9Y2I8', 'Q9NVM6', 'Q71RS6', 'P32456', 'O60760', 'Q8WV28', 'O14522', 'Q9Y2L9', 'P20809', 'Q8N2M8', 'P49716', 'Q14849', 'Q8NB16', 'Q8IUR7', 'Q9NTI5', 'Q66GS9', 'Q969N2', 'Q6ZMQ8', 'Q0ZGT2', 'Q5T0T0', 'P01123', 'P41439', 'Q9JIY5', 'O95755', 'Q71RC2', 'P57081', 'Q08AG7', 'Q68DV7', 'Q14494', 'Q9Y5L4', 'O75822', 'Q8N1W1', 'Q9BYD2', 'Q3MHD2', 'Q08285', 'Q13637', 'O95372', 'Q96D71', 'P63211', 'Q96AJ1', 'Q8NHP6', 'Q8N0W3', 'Q14157', 'Q8NF91', 'P07814', 'Q8N1F7', 'O15047', 'P63313', 'Q08235', 'Q7Z6J4', 'P32892', 'Q8CJG0', 'P22059', 'Q9HCG8', 'Q9QX74', 'Q8N3F8', 'Q9Y4D7', 'Q6VMQ6', 'P10916', 'Q86XK7', 'Q96PP9', 'Q9BY67', 'Q93099', 'P14866', 'Q9NXL9', 'O55222', 'Q00G26', 'Q9HCQ7', 'P22674', 'Q9NZL3', 'Q9BXI3', 'O95741', 'P29083', 'Q96J87', 'Q8NHY0', 'A6NM10', 'Q9Y5A7', 'Q9H6L5', 'P03211', 'Q9Y253', 'P04908', 'Q8WVK2', 'Q8NET5', 'P35869', 'Q08623', 'Q96EQ8', 'Q86UW2', 'Q8IWV8', 'P54709', 'P78543', 'Q9BY79', 'Q04837', 'Q9NFU0', 'P29469', 'O88509', 'Q13009', 'Q10113', 'Q8NI35', 'Q13873', 'Q2HR75', 'P60422', 'O15520', 'Q16773', 'O16850', 'Q9C0D3', 'Q86TD4', 'P62068', 'O43314', 'O15480', 'O75251', 'P54821', 'Q9Y5X5', 'Q5T5Y3', 'Q9Y613', 'Q5HY92', 'Q8IV50', 'Q96QD8', 'Q01432', 'Q7Z2X7', 'Q5T5U3', 'P31327', 'Q9H222', 'P12883', 'Q9H6E4', 'Q9UJA3', 'Q9HBJ8', 'P51606', 'Q8N111', 'Q8NG31', 'Q8NEA5', 'Q16626', 'P33897', 'Q9WTI7', 'Q9Z2X8', 'Q9BZM5', 'P25847', 'Q9NZU5', 'Q9NXJ0', 'O14593', 'P54198', 'Q9Y4K0', 'P38886', 'P06931', 'P50213', 'Q9JI18', 'O15042', 'Q8NFG4', 'P30999', 'Q5T0N5', 'Q9BXJ9', 'Q14168', 'P59632', 'Q9VMA3', 'Q8CIG8', 'Q80UE6', 'P49257', 'Q9H6S0', 'P70211', 'O60635', 'P35244', 'P39109', 'O95670', 'Q8TDN2', 'P35557', 'O15194', 'Q14934', 'Q96NZ8', 'Q9NYU1', 'Q9UBW5', 'O60258', 'P48145', 'Q6UWE3', 'Q96K83', 'O75448', 'P35052', 'O75310', 'Q9UIC8', 'Q9UGQ3', 'Q9BW04', 'Q5T890', 'Q494X3', 'Q6NZ63', 'Q9NWA0', 'P29728', 'Q9HB09', 'P10301', 'Q9NWB6', 'P23381', 'Q53R12', 'Q9H5L6', 'Q9UBI6', 'P14416', 'Q9Y6M7', 'Q96MC5', 'Q9NRP0', 'P14621', 'P56589', 'Q6ZV65', 'P78381', 'Q9H840', 'Q9C0K7', 'Q9H5V7', 'Q6UXU4', 'P17643', 'P36402', 'Q5VU69', 'Q6P4R8', 'Q9H981', 'P30927', 'O75081', 'Q8N0S6', 'Q9NU23', 'Q5TCX8', 'P05015', 'Q12840', 'P45985', 'O35433', 'Q9UBP0', 'P40555', 'O60218', 'Q9P0I2', 'Q8WV22', 'Q96F46', 'P97465', 'Q15389', 'Q8TC21', 'Q9NSN8', 'Q99622', 'Q99638', 'B7UI22', 'P51123', 'Q8WW59', 'P53905', 'P9WF09', 'Q2I0M4', 'P0DTF1', 'P10588', 'Q9H7B2', 'Q96PU9', 'P11499', 'Q9H469', 'Q7Z6J0', 'Q7RTV2', 'P97792', 'Q62074', 'P08152', 'Q9NYZ4', 'O94762', 'O00198', 'P13379', 'Q15004', 'P97377', 'Q9NYY1', 'Q9NVM9', 'Q6U7R4', 'Q9WTX6', 'P98084', 'Q9NYG8', 'Q8IXS6', 'P55058', 'Q9Y6Q5', 'Q8K4K2', 'Q8H2D5', 'Q58A44', 'Q96N20', 'Q8BHJ5', 'Q8N565', 'P05177', 'Q9H867', 'Q7Z4N2', 'Q6ZT98', 'Q86V24', 'Q969T7', 'O95232', 'P28161', 'Q04727', 'Q9NZV5', 'Q96RL7', 'O43299', 'O95977', 'Q8WXR4', 'Q9P215', 'P19387', 'Q9ULC0', 'Q62848', 'Q9BQ61', 'Q7Z401', 'Q9P0M9', 'Q04446', 'Q7Z6K4', 'Q8TEM1', 'Q6H9L7', 'Q8NHP8', 'P12270', 'Q9Y4C4', 'Q8WWZ1', 'Q96RD1', 'Q9Y5Y3', 'Q0VAK6', 'Q9NZ53', 'Q86YZ3', 'P02818', 'P60022', 'Q9H9V9', 'P0DPD6', 'Q15771', 'Q06732', 'Q5UIP0', 'P0C205', 'Q9NY33', 'P22315', 'P49006', 'Q1ED39', 'P41594', 'Q9BZG1', 'O76027', 'Q7Z7B7', 'Q14CB8', 'Q9M7Q7', 'Q14397', 'P56706', 'Q9Y397', 'Q9NY15', 'P23945', 'Q5VWJ9', 'Q93084', 'Q5T2S8', 'Q9P2N7', 'Q5H9L2', 'Q15048', 'O60931', 'P24311', 'P09210', 'Q86XD5', 'P47989', 'P55082', 'P50225', 'P05204', 'Q9BZM6', 'P35251', 'P46151', 'O60381', 'P51511', 'P9WHT9', 'P12307', 'A6NGK3', 'O95084', 'Q9H4Z2', 'Q969F9', 'Q96T52', 'Q96N76', 'O70583', 'P02557', 'Q923S6', 'Q5EE01', 'Q7Z6I6', 'P35499', 'Q6P0A1', 'Q9UBQ7', 'Q9TY96', 'Q96B33', 'P53954', 'P01558', 'P49070', 'P06933', 'P49683', 'Q9BXB4', 'Q4LDG9', 'P36618', 'Q8WWI1', 'P30613', 'Q9UBN4', 'P06242', 'P56199', 'P04663', 'Q6WKZ7', 'Q9WU22', 'Q5TEU4', 'P53900', 'Q709F0', 'Q69027', 'Q24JQ0', 'Q9BT04', 'Q8TCT1', 'P20536', 'Q07478', 'Q8N144', 'Q77M43', 'Q9QY40', 'Q9W0S8', 'Q9H633', 'Q5T764', 'P53152', 'Q3V0Q6', 'Q9Y5B0', 'Q94251', 'O94880', 'Q9Y6R9', 'Q9NRD8', 'P49753', 'O60508', 'Q6ZV89', 'Q5VU92', 'Q8IUQ0', 'P35749', 'P28067', 'O00230', 'P33399', 'Q96F44', 'P51911', 'Q8ND04', 'Q9DGN1', 'Q99PM9', 'P10911', 'P04062', 'Q96NL8', 'P10216', 'Q9UBZ9', 'Q76L83', 'Q8C2S0', 'B0S733', 'Q6QNK2', 'P47900', 'Q9D8X5', 'Q9H8H0', 'Q8JL80', 'P26006', 'Q86VX2', 'Q9SR06', 'Q8NI29', 'Q7Z7M8', 'P13008', 'O13016', 'P62955', 'P32592', 'P79621', 'Q8NCT1', 'O13836', 'P06927', 'Q14507', 'P19811', 'A0A663DJA2', 'Q8WYR4', 'Q12052', 'O75096', 'Q9HC23', 'Q9NPI5', 'Q05652', 'Q5SZK8', 'P38274', 'P95493', 'G5EDT1', 'O43304', 'Q96T68', 'P55145', 'Q9UBU6', 'Q66HV9', 'Q9P0U1', 'Q8BVM4', 'P31997', 'O13339', 'Q5MY95', 'Q6IUF9', 'Q9H0W5', 'Q93096', 'O08807', 'P34331', 'P06865', 'Q96S66', 'P53893', 'Q8NHV1', 'O35144', 'Q8NA29', 'Q9Y5N5', 'Q8JGS1', 'P35963', 'Q3KSR9', 'Q96DU9', 'Q8A1G2', 'Q99KQ4', 'P56528', 'P28472', 'P23895', 'O94804', 'Q06278']

st.title('HIV Protein Predictor')

protein = st.selectbox('Select Protein',sorted(proteins))

if st.button('Predict'):
    df_new1 = df[df['Entry'] == protein]
    df_new1 = df_new1.drop(['Entry', 'LABEL'], axis=1)
    result = lr.predict(df_new1)[0]
    if result == 1:
        st.header(protein + " - HIV Positive")
    if result == 0:
        st.header(protein + " - HIV Negative")



