from TestCases.NVSK.Program.Nishtha import program_nishtha


class Program_one:

    @staticmethod
    def test_run_first_script(self):
        fm = program_nishtha(self.driver)
        res = fm.test_click_the_nishitha_button()
        assert res == 0
