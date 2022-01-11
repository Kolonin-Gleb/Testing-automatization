class TestLessonCreate():
    # номер 5
    def test_create_lesson(self, browser): # Будет распознан как тест
        pass

    # номер 6
    def user_with_lesson_can_create_lesson_from_navbar_test(self, browser):
        pass


class CourseCreate():
    # номер 7
    def test_create_course(self, browser): # Не будет распознан как тест,
	# т.к. находится в классе имя которого на начинается с Test
        pass

# номер 8
def test_guest_can_open_new_course(browser): # Будет распознан как тест
    pass

