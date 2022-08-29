import logging
import traceback
import time

from Page_DMS import Operation as op
from ReadData_DMS import ReadDatas as rd
import pytest


class TestDms:

    def setup(self):
        try:
            self.op = op.test1()
        except:
            logger = logging.getLogger(__name__)
            formatter1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh = logging.FileHandler("log/"+str(time.time()) + '.txt',encoding='utf-8')
            fh.setFormatter(formatter1)
            logger.addHandler(fh)
            logger.error(traceback.format_exc())
            logger.info(123)


    @pytest.mark.parametrize('param', rd.qiangbao())
    def test_one(self, param):
        # self.op.buttonclick("请输入vin码", "LZTPG4YA7SQ000069")

        self.op.buttonclick("VIN码", "LZTPG4YA7SQ000069")
        for i in range(0, len(param), 2):
            self.op.buttenorselect1(param[i], param[i + 1])
        self.op.upload()
        self.op.end_save()

    def terndown(self):

        self.op.wb.close()
