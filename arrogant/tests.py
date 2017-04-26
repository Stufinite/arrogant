from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

# Create your tests here.
class SlothTestCase(TestCase):
	fixtures = ['arrogant.json']
	def setUp(self):
		self.client = Client()

	def test_clist(self):
		response = self.client.get(reverse('arrogant:jlist')+"?location=台南市東區&start=1")
		self.assertEqual(response.json(), [{'pk': 754, 'model': 'arrogant.job', 'fields': {'實習時段': '暑期實習、學期實習、學年實習', 'job': '台南遠百店-涮乃葉 內外場計時人員(實習', '休假制度': '排休, 輪休', '工作地點': '台南市東區 前鋒路210號四樓(大遠百', '工作時間': '日班, 中班, 晚班, 假日班, 輪', '身份類別': '一般求職者／日間就學中', '薪資': '時薪\xa0133至150', '職缺更新': '2017/4/19', '職務類別': '餐飲服務人員、餐廚助手', '工作說明': '「涮乃葉」為雲雀在台開幕之新品牌歡迎您加', '聯絡人員': '林店長', 'fromWitchWeb': '1111', 'avatar': 'maid_BwdsckP.png', '地區': '台南市東區', '需求人數': '不限', 'url': 'http://www.1111.com.tw/job-bank/job-description.asp?eNo=79117525&agent=internships', '工作經驗': '不拘', '學歷限制': '不拘', '工作性質': '兼職、企業實習', 'company': 1006, '科系限制': '不拘', '到職日期': '不限'}}])

	def test_cvalue(self):
		response = self.client.get(reverse('arrogant:jvalue')+'?id=754')
		self.assertEqual(response.json(), {'工作性質': '兼職、企業實習', 'avatar': '/media/maid_BwdsckP.png', '工作時間': '日班, 中班, 晚班, 假日班, 輪', '職務類別': '餐飲服務人員、餐廚助手', '職缺更新': '2017/4/19', 'id': 754, '實習時段': '暑期實習、學期實習、學年實習', 'job': '台南遠百店-涮乃葉 內外場計時人員(實習', '工作說明': '「涮乃葉」為雲雀在台開幕之新品牌歡迎您加', '身份類別': '一般求職者／日間就學中', '工作地點': '台南市東區 前鋒路210號四樓(大遠百', '地區': '台南市東區', '工作經驗': '不拘', '科系限制': '不拘', '到職日期': '不限', 'url': 'http://www.1111.com.tw/job-bank/job-description.asp?eNo=79117525&agent=internships', '聯絡人員': '林店長', '薪資': '時薪\xa0133至150', '學歷限制': '不拘', '需求人數': '不限', 'company': '雲雀國際股份有限公司', '休假制度': '排休, 輪休', 'fromWitchWeb': '1111'})

	def test_search(self):
		response = self.client.get(reverse('arrogant:recommendJvalue')+"?school=nchu&dept=U56&degree=3")
		self.assertEqual(response.status_code, 200)

	def test_comment(self):
		response = self.client.get(reverse('arrogant:comment')+"?id=754&start=1")		
		self.assertEqual(response.json(), [{"model":"arrogant.comment","pk":1,"fields":{"Job":754,"create":"2017-04-24T11:54:42Z","raw":"測試測試"}},{"model":"arrogant.comment","pk":2,"fields":{"Job":754,"create":"2017-04-24T14:13:08.788Z","raw":"這是測試"}},{"model":"arrogant.comment","pk":3,"fields":{"Job":754,"create":"2017-04-24T14:19:11.154Z","raw":"測試第三次XD"}}])