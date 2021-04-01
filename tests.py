import unittest
from app import app


class TestIndex(unittest.TestCase):
    def setUp(self):
        self.app_test = app.test_client()
        self.response = self.app_test.get('/')

    def test_get_index_returns_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_get_index_renders_html(self):
        self.assertIn('text/html', self.response.content_type)

    def test_get_index_renders_title_html(self):
        response_decoded = self.response.data.decode('utf-8')
        self.assertIn('<title>Página Inícial</title>', response_decoded)


class TestInsert(unittest.TestCase):
    def setUp(self):
        self.app_test = app.test_client()
        self.response = self.app_test.get('/insert')

    def test_get_insert_returns_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_get_insert_renders_html(self):
        self.assertIn('text/html', self.response.content_type)

    def test_get_index_renders_title_html(self):
        response_decoded = self.response.data.decode('utf-8')
        self.assertIn('<title>Criar nova Tarefa</title>', response_decoded)


class TestFindAll(unittest.TestCase):
    def setUp(self):
        self.app_test = app.test_client()
        self.response = self.app_test.get('/find-all')

    def test_get_find_all_returns_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_get_find_all_renders_html(self):
        self.assertIn('text/html', self.response.content_type)

    def test_get_index_renders_title_html(self):
        response_decoded = self.response.data.decode('utf-8')
        self.assertIn('<title>Lista de Tarefas</title>', response_decoded)


if __name__ == '__main__':
    unittest.main()
