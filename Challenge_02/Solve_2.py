def isInvalidLog(log):
    flag = False
    max = 0
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    last_letter_pos = 0
    for i in log:
        if i not in alphabet:
            if int(i) < max or flag:
                return True
            max = int(i)
        else:
            flag = True
            if alphabet.index(i) < last_letter_pos:
                return True
            last_letter_pos = alphabet.index(i)
        
    return False

if __name__ == '__main__':
    log_list = ['03345678', 'ijpx', 'se35', 'rmkvy', '0469giz', '0014559', 'aadffgt', 'yb408', 'rejwg', '077cfv', '0378', 'fjjjq', 'skta1912', 'a7d2vo', '4588hnr', '0469', 'hhhknsty', 'rjqf2915', 'c1am', '378af', '2569', 'bbdjstu', 'svf7241', 'bmkqzd', '129eox', '126999', 'abbggrt', 'lhv9725', 'ktjv', '2467hhq', '023789', 'chmwz', 'gh58', 'qrgmf', '2889dfls', '011235', 'crrrs', 'rv042', '2r8pzw', '2468kqw', '01146777', 'fghu', 'uzw378', 'yrh1fg0', '0158rxz', '2346789', 'dllnorr', 'mr84', '97fk7wq', '0479fgs', 'fmnu', 'vcn191', '8iqfp3tj', '2268lwz', '23366799', 'bhhitwy', 'hn30', 'k5cw', '1367bdkw', '223679', 'hjkm', 'efc472', 'nzxmz', '0034aghv', '012567', 'bbfglrrs', 'iey5099', 'f64b3', '357dm', '0112369', 'acnotz', 'op52', 'ygow8gr', '45cl', '1122466', 'fintx', 'qvo3239', 'qdixk0h', '06fy', '01446678', 'klnty', 'at33', '2u95xkh6', '115tty', '23355779', 'aeginqtx', 'mnl939', 'nail', '45ak', '04569', 'bclnqqwz', 'tsyz0761', 'qrpv5a9a', '059hks', '01457', 'cfilqvxx', 'mjap6288', 'a19lsnz', '156dn', '1679', 'hjjlouy', 'csb697', '9c68', '0023aexx', '134456', 'aggtuz', 'dyqe7601', 'moyl', '0068guvy', '01578', 'glqssuy', 'qw665', 'nqno', '08hv', '33335889', 'qqsuz', 'pp28', 'np8zevb', '78jv', '3469', 'aailmps', 'cnfs2459', '2cwhs036', '389iwy', '5677', 'gghjn', 'bg02', 'z5iysbm', '457gi', '1188899', 'lnrruy', 'woz173', 'kqasj', '1257dnr', '0134', 'ghkr', 'ew129', 'caykz', '3557cdru', '013489', 'cgixz', 'ol481', 'ejiaydio', '5699ddt', '3346', 'absvy', 'zh824', 'imeh658', '09jv', '12268', 'addhsz', 'toze0819', '337f', '024hht', '1113', 'cequ', 'ysg0699', '31qxo1l1', '235blz', '33667', 'ghmnqq', 'rx100', '5piyd', '07bp', '2599', 'dikmvw', 'gp460', 'cq4w4pk', '2479cgm', '0223599', 'gkosz', 'pxc633', 'qha82', '4678apt', '1222359', 'llmnpx', 'tka881', '13au7rzt', '08ft', '044788', 'bcekltvw', 'uwwe3624', '6s3y5r', '16bl', '25789', 'aboppqzz', 'op695', '3h7nf', '337bx', '01123589', 'llmqsy', 'jym741', '3r68bdk', '2788kmpt', '226669', 'afnorxyz', 'va88', '0tu7l', '448pz', '013799', 'stuz', 'vtq1615', 'rzjjl', '0128imnx', '3789', 'bdjmpt', 'bny6434', '46j3', '19fx', '0234', 'efiimpq', 'he063', 'galeealv', '046jo', '015577', 'ktuy', 'ox21', 'xdpwvi', '2246elnt', '2566', 'ghjmmoz', 'aps226', 'nw87e', '039cy', '14588', 'abdiity', 'gza610', 'a6gi', '589dgx', 'bnooqzz', 'tii616', 'lw3q', '347mps', '024556', 'affgqty', 'ww128', '68ktou', '0367eoru', '457899', 'ejloosyz', 'wia8680', '5yy98f', '57ht', '57888', 'hhjlouwy', 'yw388', 'nc32o8', '0256mwz', '0444899', 'fffjv', 'ayu672', 'm2iq63', '3489jluv', '01357788', 'chlrwz', 'euby8162', 'x1jb', '779ac', '013467', 'nsxz', 'tf99', 'tgr8i', '2234gkmy', '37888', 'aaehqtww', 'aaz773', '2rdfd40', '0356hjtw', '123678', 'dhjxzz', 'jvs8920', 'rejt', '0338bdes', '2248', 'deerwz', 'glr6248', 'oo6l', '26qu', '0335', 'ahttxy', 'wr410', '36mu', '247ghl', '00335', 'bfgku', 'qc00', 'epugx', '016hjt', '34578', 'abcfnv', 'zqgs4949', 'smfei', '0266cen', '23359', 'ajkoswyy', 'rhrm2663', '9wm4', '246fsy', '2334', 'lstz', 'nu835', 'o1btvc', '0045egiq', '12279', 'agppv', 'tpa049', '1ppx', '1389dhox', '00556899', 'agmppx', 'ucv091', 'g8fmx9cc', '499gk', '01144778', 'himw', 'tkw1469', 'hl1rpwf', '68dh', '1578999', 'oouvxz', 'brd074', 'jcnk7ph', '5557krsv', '1457', 'jors', 'hkt601', 'x9kjlpj', '88ov', '1344577', 'chjquvxz', 'pkd8881', 'knk9', '46qu', '000668', 'cdemrsv', 'nge4032', 'jniteqgs', '3389ioot', '1357788', 'ehmmp', 'pkv473', 'p46ktk', '15hj', '02233', 'fjkkt', 'wzla0079', 'i3c9r7n', '0347bgr', '0124445', 'bnqrssw', 'fen6894', '7gj3', '4467aix', '34458', 'adfqtvvx', 'bci6836', 'mvzh', '0166fiks', '02338899', 'ijlnootx', 'mj76', '3ek7oarr', '4677ansu', '35567', 'bdgjjrrz', 'mzcn0818', 'y6grtw3p', '1357gmp', '144479', 'bfmp', 'loo946', 'xhp4a', '1444clsy', '0345558', 'bhikuvy', 'yp57', 'ryg3dnk7', '6889jlx', '00015689', 'ghlnuuv', 'ktky4928', 'f9de', '002cq', '5888', 'fnprvwy', 'vszk1907', 'r94cu', '014gn', '45688', 'cfikkkty', 'mvw517', 'v6yy', '124cei', '015778', 'bgqrwz', 'tuu595', 'm0idt2l', '2447gisy', '0047', 'bhmoqss', 'beo9166', '1k1v6', '0268fhlt', '33447999', 'cfhr', 'xdx8595', 'l59vv62b', '139flv', '3578', 'bhkmqrtw', 'jng386', '9zif01d', '1466ikox', '1344478', 'akmm', 'ccm5112', 'lv7cjv', '048mx', '023799', 'hikox', 'kekz0942', '7hwrzw9r', '069am', '223355', 'efhhpz', 'kgm693', 'q25a6qo', '124mnv', '233478', 'bdfhlsu', 'nga491', '4bnf', '1245nwyz', '033379', 'hikknpuw', 'swm0799', 'f3fkd', '346bp', '2444468', 'elpq', 'jp49', 'uz7chq', '0129ffhx', '003369', 'huvwyy', 'bn749', 'lf7mv2e', '1449pqy', '2468', 'fgkqruuua', 'qkh720', 'ocamx', '0145ghnv', 'clmoowxy', 'do00', '1snxwb', '0199pwz', '03578', 'dffmsvx', 'qd524', 'otrscz', '66mw', '01234', 'iijlqt', 'xw67', 'bewv', '058npz', '3568', 'beiilst', 'rdu268', 'qro1fujj', '79an', '3334778', 'ijnpqvx', 'udms5941', 'kn5g', '0003ltx', '2446678', 'acgptu', 'rrr583', 'uyeweze', '1347ghkp', '1137', 'fjjnovz', 'ici7617', 'l241ju9', '1678osx', '03688', 'bbbfmmy', 'lqe001', 'yl3bit', '2268aot', '12377789', 'efhpww', 'gff6718', 'y6269zk', '0349inno']

    real = 0
    machine = 0
    for log in log_list:
        if isInvalidLog(log):
            machine += 1
        else:
            real += 1
    print(isInvalidLog('gh58'))
    print(f'{real}true{machine}false')
        