import hw2
import random
import unittest

# From Nicholas Qiao
nq_instance0 = {
  'Amumu': ('4','8','5','13'),
  'Darius': ('11','2','2','0'),
  'Evelynn': ('15','7','7','0'),
  'Elise': ('10','17','6','8'),
  'Blitzcrank': ('12','18','13','12'),
  'Ashe': ('15','14','4','1'),
  'Brand': ('0','2','15','12'),
  'Dr.Mundo': ('1','0','9','15'),
  'Corki': ('3','8','8','10'),
  'ChoGath': ('5','6','18','1'),
  'Cassiopeia': ('11','13','14','12'),
  'Anivia': ('12','4','19','3'),
  'Diana': ('14','19','8','14'),
  'Ahri': ('17','16','12','11'),
  'Annie': ('13','9','10','12'),
  'alphabetAatrox': ('3','5','14','8'),
  'Draven': ('10','7','14','14'),
  'Akali': ('19','1','1','2'),
  'Alistar': ('6','9','11','12'),
  'Caitlyn': ('16','18','11','9')
}

def remove_dup(stu_avail):
    ret = {}
    for stu, shifts in stu_avail.iteritems():
        ret[stu] = tuple(set(shifts))
    return ret

nq_instance = remove_dup (nq_instance0)

def RandomInstance(num_pairs, difficulty, seed):
  assert 0 <= difficulty/num_pairs <= 1
  random.seed(seed)

  n = num_pairs * 2
  ret = {}
  for i in range(n):
    ret['S%d' % i] = [
        str(j) for j in range(n) if random.random() <= difficulty / num_pairs]
  return ret


class Test(unittest.TestCase):
  def CheckValidSolution(self, student_availabilities, time_slots):
    slots = set()
    for student, times in student_availabilities.items():
      slots.update(times)
    for slot in sorted(slots):
      self.assertIn(slot, time_slots)
      self.assertEqual(2, len(time_slots[slot]))
      student0, student1 = time_slots[slot]
      self.assertNotEqual(student0, student1)
      self.assertIn(slot, student_availabilities[student0])
      self.assertIn(slot, student_availabilities[student1])

  def test_nq_instance(self):
    self.CheckValidSolution(nq_instance, hw2.Solve(nq_instance))

  def test_simple_example(self):
    example = {'Alice': ('0', '1', '2', '3'), 'Bob': ('1', '2'),
        'Charlie': ('2', '3'), 'Denise': ('3', '0')}
    correct_result = {'0': ('Alice', 'Denise'), '1': ('Alice', 'Bob'),
        '2': ('Bob', 'Charlie'), '3': ('Charlie', 'Denise')}
    result = hw2.Solve(example)
    for slot in '0123':
      assert(slot in result)
      self.assertEqual(correct_result[slot], tuple(sorted(result[slot])))

  def test_random4(self):
    availabilities = RandomInstance(5, 4.0, 1)
    self.CheckValidSolution(availabilities, hw2.Solve(availabilities))

  def test_random5(self):
    availabilities = RandomInstance(5, 2.0, 4)
    self.CheckValidSolution(availabilities, hw2.Solve(availabilities))

  def test_random6(self):
    availabilities = RandomInstance(10, 8.0, 3)
    self.CheckValidSolution(availabilities, hw2.Solve(availabilities))

  def test_random7(self):
    availabilities = RandomInstance(10, 4.0, 4)
    self.CheckValidSolution(availabilities, hw2.Solve(availabilities))

  def test_random8(self):
    availabilities = RandomInstance(20, 4.0, 5)
    self.CheckValidSolution(availabilities, hw2.Solve(availabilities))

  def test_random9(self):
    availabilities = RandomInstance(20, 4.0, 6)
    self.CheckValidSolution(availabilities, hw2.Solve(availabilities))

  def test_random10(self):
    availabilities = RandomInstance(30, 8.0, 7)
    self.CheckValidSolution(availabilities, hw2.Solve(availabilities))

  def test_random11(self):
    availabilities = RandomInstance(30, 8.0, 8)
    self.CheckValidSolution(availabilities, hw2.Solve(availabilities))


if __name__ == '__main__':
  unittest.main()
