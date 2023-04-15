
    
    def test_add(self):
        result=calc.add(10,5)
        self.assertEqual(result,15)
    def test_sub(self):
        result=calc.sub(10,5)
        self.assertEqual(result,5)
    def test_mul(self):
        result=calc.mul(10,5)
        self.assertEqual(result,50)
    def test_div(self):
        result=calc.div(10,5)
        self.assertEqual(result,2)
    def test_mod(self):
        result=calc.mod(20,5)
        self.assertEqual(result,2)
    

