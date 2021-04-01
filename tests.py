import unittest

from app import app, find_by_description, find_by_id


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


class TestFindAll(unittest.TestCase):
    def setUp(self):
        self.app_test = app.test_client()
        self.response = self.app_test.get('/find-all')

    def test_get_find_all_returns_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_get_find_all_renders_html(self):
        self.assertIn('text/html', self.response.content_type)

    def test_get_find_all_renders_title_html(self):
        response_decoded = self.response.data.decode('utf-8')
        self.assertIn('<title>Lista de Tarefas</title>', response_decoded)


class TestInsert(unittest.TestCase):
    def setUp(self):
        self.app_test = app.test_client()
        self.response = self.app_test.get('/insert')

    def test_get_insert_returns_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_get_insert_renders_html(self):
        self.assertIn('text/html', self.response.content_type)

    def test_get_insert_renders_title_html(self):
        response_decoded = self.response.data.decode('utf-8')
        self.assertIn('<title>Criar nova Tarefa</title>', response_decoded)

    def test_create_register_in_database(self):
        description = 'TesteInsert'
        status = False
        self.app_test.post('/insert', data=dict(description=description, status=status))
        task = find_by_description(description)

        self.assertEqual(description, task.description)
        self.app_test.delete('/delete-by-id/' + str(task._id))


class TestUpdate(unittest.TestCase):
    def setUp(self):
        self.app_test = app.test_client()

    def test_update_register_in_database(self):
        description = 'TesteUpdate'
        status = False
        self.app_test.post('/insert', data=dict(description=description, status=status))
        task = find_by_description(description)

        description = 'TesteUpdateUpdated'
        self.app_test.put('/update-by-id/' + str(task._id), data=dict(description=description))
        task = find_by_description(description)

        self.assertEqual(description, task.description)
        self.app_test.delete('/delete-by-id/' + str(task._id))

    def test_update_status_of_register_in_database(self):
        description = 'TesteUpdateStatus'
        status = False
        self.app_test.post('/insert', data=dict(description=description, status=status))
        task = find_by_description(description)
        self.app_test.put('/change-status-by-id/' + str(task._id))
        task = find_by_id(task._id)

        self.assertEqual(True, task.status)
        self.app_test.delete('/delete-by-id/' + str(task._id))


class TestDelete(unittest.TestCase):
    def setUp(self):
        self.app_test = app.test_client()

    def test_delete_register_in_database(self):
        description = 'TesteDelete'
        status = False
        self.app_test.post('/insert', data=dict(description=description, status=status))
        task = find_by_description(description)

        self.app_test.delete('/delete-by-id/' + str(task._id))
        task = find_by_description(description)

        self.assertEqual(None, task)


if __name__ == '__main__':
    unittest.main()
