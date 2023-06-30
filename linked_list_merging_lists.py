def merge_sorted(head1, head2):
  # if both lists are empty then merged list is also empty
  # if one of the lists is empty then other is the merged list
  if head1 == None:
    return head2
  elif head2 == None:
    return head1

  # new list to be added to
  mergedHead = None;

  # first check which value between the two is smaller
  if head1.data <= head2.data:
    # start the list
    mergedHead = head1

    # advance the pointer to the next item in the list
    head1 = head1.next
  else:
     # start the list
    mergedHead = head2

    # advance the pointer to the next item in the list
    head2 = head2.next

  # initially the tail and the head are the same until more items are added
  mergedTail = mergedHead

  # while head1 is not null and head2 is not null, continue
  while head1 != None and head2 != None:
    # start with an empty temp var
    temp = None
    # same check if left side is smaller than right side
    if head1.data <= head2.data:
      # record the current head object
      temp = head1

      # move the item further in the list
      head1 = head1.next
    else:
      temp = head2
      head2 = head2.next

    # the merged tail is now the NEW temp object, temp should be the larger of the two ints being compared
    mergedTail.next = temp
    mergedTail = temp

  # if the head has a value and you're here, the loop is over and maybe you have a whole section of values which are larger which you'll just link to
  if head1 != None:
    mergedTail.next = head1
  elif head2 != None:
    mergedTail.next = head2

  return mergedHead
