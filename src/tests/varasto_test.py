import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_varaston_jossa_negatiivisen_tilavuus_ja_saldo(self):
        self.varasto2= Varasto(-10,-10)
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)
        self.assertAlmostEqual(self.varasto2.saldo, 0)
    
    def test_konstruktori_luo_varaston_jossa_saldo_suurempi_kuin_tilavuus(self):
        self.varasto2= Varasto(100,111)
        self.assertAlmostEqual(self.varasto2.tilavuus, 100)
        self.assertAlmostEqual(self.varasto2.saldo, 100)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_saldo_ei_kasva_yli_tilavuuden(self):
        tilavuus=self.varasto.tilavuus
        self.varasto.lisaa_varastoon(tilavuus+100)
        self.assertEqual(self.varasto.saldo, tilavuus)
    
    def test_lisaa_negatiivinen_määrä_ei_muuta_saldoa(self):
        saldo_aluksi=self.varasto.saldo
        self.varasto.lisaa_varastoon(-10)
        self.assertEqual(self.varasto.saldo, saldo_aluksi)
    
    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivisen_maaran_ottaminen_ei_muuta_saldo(self):
        saldo_aluksi=self.varasto.saldo
        self.varasto.ota_varastosta(-10)
        self.assertEqual(self.varasto.saldo, saldo_aluksi)
    
    def test_ei_voi_ottaa_enempaa_kuin_saldo(self):
        saldo_aluksi=self.varasto.saldo
        saatu_maara = self.varasto.ota_varastosta(saldo_aluksi+1)
        self.assertEqual(saatu_maara, saldo_aluksi)
    
    def test_tulostus(self):
        saldo=self.varasto.saldo
        mahtuu=self.varasto.paljonko_mahtuu()
        self.assertEqual(self.varasto.__str__(), f"saldo = {saldo}, vielä tilaa {mahtuu}")