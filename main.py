
def count_batteries_by_health(present_capacities):
  rated_capacity=120
  healthy=0
  exchange=0
  failed=0
  
  #condition for checking category 
  for i in present_capacities:
    SoH=(i/rated_capacity)*100
    if(SoH>80 and SoH<=100):
      healthy=healthy+1
    elif(SoH>=62 and SoH<=80):
      exchange=exchange+1
    else:
      failed=failed+1
    
  return {
    "healthy": healthy,
    "exchange": exchange,
    "failed": failed
  }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)

  #Addition boundary test cases
  additional_test_cases=[96,120,74.4]
  additional_test_count=count_batteries_by_health(additional_test_cases)
  
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
