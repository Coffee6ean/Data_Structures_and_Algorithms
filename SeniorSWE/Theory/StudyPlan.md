# Updated Senior Full-Stack Developer Study Plan - DSA Focus

## 🚨 **PRIORITY 1: DSA Patterns (Daily Practice - 8 weeks)**

### **The 17 Core Patterns That Cover 95% of FAANG Questions** 
*Updated based on 2025 Amazon assessment data - including the patterns that "folded" you*

#### **Week 1-2: Foundation Patterns (Master These First)**
1. **Two Pointers** ⭐⭐⭐
   - *Amazon Frequency: Very High*
   - **Master Problems:**
     - Two Sum II (167) - *Easy warmup*
     - Container With Most Water (11) - *Amazon favorite*
     - 3Sum (15) - *Core pattern*
     - Trapping Rain Water (42) - *Hard but common*
   - **Pattern Recognition:** Sorted arrays, finding pairs/triplets, opposite direction searching

2. **Sliding Window** ⭐⭐⭐
   - *Amazon Frequency: Very High*
   - **Master Problems:**
     - Maximum Average Subarray I (643) - *Easy start*
     - Longest Substring Without Repeating Characters (3) - *Amazon classic*
     - Minimum Window Substring (76) - *Hard but frequent*
     - Sliding Window Maximum (239) - *Deque technique*
   - **Pattern Recognition:** Contiguous subarrays, substring problems, "maximum/minimum in window"

3. **Fast & Slow Pointers (Floyd's Cycle)** ⭐⭐
   - *Amazon Frequency: Medium-High*
   - **Master Problems:**
     - Linked List Cycle (141) - *Foundation*
     - Find the Duplicate Number (287) - *Amazon loves this*
     - Happy Number (202) - *Cycle detection*
     - Linked List Cycle II (142) - *Find cycle start*
   - **Pattern Recognition:** Cycle detection, finding middle elements, "tortoise and hare"

#### **Week 3-4: Tree & Graph Patterns**
4. **Tree Traversal (DFS/BFS)** ⭐⭐⭐
   - *Amazon Frequency: Very High*
   - **Master Problems:**
     - Binary Tree Inorder Traversal (94) - *Foundation*
     - Maximum Depth of Binary Tree (104) - *Easy DFS*
     - Binary Tree Level Order Traversal (102) - *BFS classic*
     - Binary Tree Right Side View (199) - *Amazon favorite*
     - Lowest Common Ancestor (236) - *Very common*
   - **Pattern Recognition:** Tree problems, level-by-level processing, parent-child relationships

5. **Binary Search** ⭐⭐⭐
   - *Amazon Frequency: Very High*
   - **Master Problems:**
     - Binary Search (704) - *Foundation*
     - Find First and Last Position (34) - *Amazon classic*
     - Search in Rotated Sorted Array (33) - *Very frequent*
     - Find Minimum in Rotated Sorted Array (153) - *Variation*
   - **Pattern Recognition:** Sorted arrays, "find target", O(log n) requirements

6. **Graph Traversal (DFS/BFS)** ⭐⭐
   - *Amazon Frequency: Medium-High*
   - **Master Problems:**
     - Number of Islands (200) - *Classic DFS*
     - Word Ladder (127) - *BFS shortest path*
     - Course Schedule (207) - *Topological sort*
     - Clone Graph (133) - *Graph traversal*
   - **Pattern Recognition:** Connected components, shortest path, graph coloring

#### **Week 5-6: Advanced Patterns**
7. **Dynamic Programming** ⭐⭐⭐
   - *Amazon Frequency: High*
   - **Master Problems:**
     - Climbing Stairs (70) - *Foundation*
     - House Robber (198) - *1D DP*
     - Coin Change (322) - *Classic DP*
     - Longest Increasing Subsequence (300) - *Amazon favorite*
     - Edit Distance (72) - *2D DP*
   - **Pattern Recognition:** Optimization problems, "maximum/minimum", overlapping subproblems

8. **Backtracking** ⭐⭐
   - *Amazon Frequency: Medium*
   - **Master Problems:**
     - Permutations (46) - *Foundation*
     - Subsets (78) - *Generate all combinations*
     - N-Queens (51) - *Classic backtracking*
     - Word Search (79) - *2D backtracking*
   - **Pattern Recognition:** "Generate all", combinations, permutations, constraint satisfaction

9. **Monotonic Stack** ⭐⭐
   - *Amazon Frequency: Medium-High*
   - **Master Problems:**
     - Next Greater Element I (496) - *Foundation*
     - Daily Temperatures (739) - *Amazon favorite*
     - Largest Rectangle in Histogram (84) - *Hard but common*
     - Trapping Rain Water (42) - *Alternative approach*
   - **Pattern Recognition:** "Next greater/smaller", stack-based solutions

#### **Week 7-8: Amazon-Specific Patterns**
10. **Heap/Priority Queue** ⭐⭐
    - *Amazon Frequency: Medium-High*
    - **Master Problems:**
      - Kth Largest Element (215) - *Foundation*
      - Top K Frequent Elements (347) - *Amazon loves this*
      - Merge k Sorted Lists (23) - *Classic heap*
      - Find Median from Data Stream (295) - *Two heaps*
    - **Pattern Recognition:** "Top K", "Kth largest/smallest", merge problems

11. **Merge Intervals** ⭐⭐
    - *Amazon Frequency: Medium*
    - **Master Problems:**
      - Merge Intervals (56) - *Foundation*
      - Insert Interval (57) - *Amazon classic*
      - Non-overlapping Intervals (435) - *Greedy approach*
      - Meeting Rooms II (253) - *Scheduling problem*
    - **Pattern Recognition:** Overlapping ranges, scheduling, time intervals

12. **Trie (Prefix Tree)** ⭐
    - *Amazon Frequency: Medium*
    - **Master Problems:**
      - Implement Trie (208) - *Foundation*
      - Word Search II (212) - *Trie + backtracking*
      - Design Add and Search Words (211) - *Trie with wildcards*
    - **Pattern Recognition:** Prefix matching, word searches, autocomplete

#### **Additional Advanced Patterns (Weeks 7-8)**
13. **Union Find (Disjoint Set)** ⭐
    - **Master Problems:** Number of Islands (200), Redundant Connection (684)
14. **Bit Manipulation** ⭐
    - **Master Problems:** Single Number (136), Counting Bits (338)
15. **Advanced String Patterns** ⭐
    - **Master Problems:** KMP Algorithm, String Matching with preprocessing

#### **CRITICAL: Amazon Assessment Revenge Patterns (Week 1 - Priority)**
**These are the exact pattern types from your failed assessment:**

16. **Subsequence Problems** ⭐⭐⭐
   - *Amazon Frequency: VERY High (You experienced this!)*
   - **Master Problems:**
     - Longest Increasing Subsequence (300) - *Foundation*
     - Longest Common Subsequence (1143) - *Classic DP*
     - Number of Longest Increasing Subsequence (673) - *Amazon loves this*
     - Distinct Subsequences (115) - *Hard but frequent*
     - Is Subsequence (392) - *Two pointer approach*
   - **Pattern Recognition:** "Find/count subsequences", "longest/shortest subsequence", dynamic programming on sequences
   - **Key Insight:** Subsequence ≠ Substring (elements don't need to be contiguous)

17. **Segmentify/Range Query Problems** ⭐⭐
   - *Amazon Frequency: High (Segment Trees, Range Queries)*
   - **Master Problems:**
     - Range Sum Query - Mutable (307) - *Segment tree foundation*
     - Range Minimum Query (RMQ) - *Core concept*
     - Count of Range Sum (327) - *Amazon assessment type*
     - Range Sum Query 2D - Mutable (308) - *2D extension*
     - My Calendar I (729) - *Segment overlap problems*
   - **Pattern Recognition:** "Range queries", "update range", "segment operations", "interval problems"
   - **Key Structures:** Segment Trees, Fenwick Trees, Prefix Sums

#### **🔥 Assessment Recovery Quick-Win Problems**
**Practice these EXACT problem types that mirror your failed assessment:**

**Subsequence Problems (Do these first!):**
- Longest Increasing Subsequence (300) - Classic DP approach
- Longest Common Subsequence (1143) - 2D DP pattern  
- Number of Distinct Subsequences (115) - Counting subsequences
- Is Subsequence (392) - Two pointer technique
- Wiggle Subsequence (376) - State machine DP

**Segmentify/Range Problems (Amazon's favorites!):**
- Range Sum Query - Mutable (307) - Segment tree implementation
- Count of Smaller Numbers After Self (315) - Fenwick tree/segment tree
- Range Addition (370) - Difference array technique
- My Calendar I/II/III (729/731/732) - Interval scheduling
- Meeting Rooms II (253) - Interval merging pattern

---

## 📚 **DSA Study Schedule with Udemy Course Integration (8 weeks)**

### **Optimal Learning Method: "Learn-Then-Implement" Approach**
*Based on senior developer recommendations - most time-efficient for interview prep*

**Daily Problem-Solving Routine (45 minutes per problem):**
1. **Watch Solution Video** (10-15 min) - Understand approach & pattern
2. **Close Everything & Implement** (20-30 min) - Code from scratch while explaining out loud
3. **Compare & Take Notes** (5-10 min) - Add to pattern recognition cheat sheet

### **Phase 1: Assessment Revenge + Foundation (Week 1-2)**
**Daily Routine (3-4 hours/day):**
- **Morning (1.5 hours):** Udemy course sections + theory
- **Afternoon (1 hour):** Watch solution videos for priority patterns
- **Evening (1.5 hours):** Implement problems using learn-then-code method

**Week 1 - Assessment Revenge Focus:**
- **Monday:** 
  - Udemy: Arrays + Two Pointers
  - **Learn-Then-Implement:** Longest Increasing Subsequence (300)
  - **Practice:** Is Subsequence (392)
- **Tuesday:** 
  - Udemy: Hash Tables + Strings
  - **Learn-Then-Implement:** Longest Common Subsequence (1143)
  - **Practice:** Number of Distinct Subsequences (115)
- **Wednesday:** 
  - Udemy: Trees + Basic DP
  - **Learn-Then-Implement:** Range Sum Query - Immutable (303)
  - **Practice:** Range Sum Query - Mutable (307) - *Watch William Fiset's segment tree video first*
- **Thursday:** 
  - **Learn-Then-Implement:** Count of Smaller Numbers After Self (315)
  - **Practice:** My Calendar I (729)
  - **Review:** All subsequence patterns learned so far
- **Friday:** 
  - **Mixed Practice:** Combine subsequence + range query problems
  - **Mock Assessment:** Time yourself on similar problems (1 hour each)
- **Weekend:** 
  - **Pattern Review:** Create cheat sheet of approaches learned
  - **Communication Practice:** Explain solutions out loud

**Week 2 - Solidify + Udemy Completion:**
- **Monday-Wednesday:** Complete remaining Udemy sections using learn-then-implement for course problems
- **Thursday-Friday:** Advanced practice on assessment patterns + communication drills
- **Weekend:** Full mock assessment simulation

### **Phase 2: Pattern-Focused Practice (Week 3-8)**
**Daily Routine (2-3 hours/day):**
- **Morning (1 hour):** New pattern study + pattern recognition
- **Evening (1-2 hours):** Practice medium/hard problems + communication practice

**Weekly Structure:**
- **Monday:** New pattern introduction using Udemy knowledge as foundation
- **Tuesday-Thursday:** Medium problems from current pattern
- **Friday:** Hard problem from current pattern
- **Saturday:** Mixed review from all learned patterns
- **Sunday:** Mock interview practice (timed problems) + communication drills

### **Amazon-Specific Focus (Post-Udemy):**
- **Week 3-4:** Two Pointers, Sliding Window, Fast & Slow Pointers
- **Week 5-6:** Tree/Graph Traversal, Binary Search (building on Udemy tree knowledge)
- **Week 7-8:** Dynamic Programming, Backtracking, Monotonic Stack
- **Week 9-10:** Heap, Merge Intervals, Trie + Mock interviews

---

## 🎯 **PRIORITY 2: DevOps Completion (Weeks 1-4)**

### **Week 1-2: Core AWS & CI/CD**
- **AWS Services:** RDS, Lambda, S3, CloudWatch, ELB
- **CI/CD:** GitHub Actions pipeline for your current projects
- **Monitoring:** CloudWatch setup + alerting
- **Security:** IAM roles, VPC, security groups

### **Week 3-4: Database & Infrastructure**
- **Database Migration:** File-based → PostgreSQL
- **Performance:** Query optimization, indexing
- **Scaling:** Load balancing, connection pooling
- **Documentation:** Infrastructure as Code (Terraform/CloudFormation)

**Time Allocation:** 1-2 hours/day (parallel with DSA morning routine)

---

## 🎯 **PRIORITY 3: TypeScript + React (Weeks 3-6)**

### **Week 3-4: TypeScript Fundamentals**
- **Core TypeScript:** Interfaces, types, generics
- **React + TypeScript:** Component typing, props, hooks
- **Best Practices:** Strict mode, type safety
- **Project:** Convert one existing React project to TypeScript

### **Week 5-6: Advanced React Patterns**
- **State Management:** Redux Toolkit with TypeScript
- **Performance:** React Query, memoization, lazy loading
- **Testing:** Jest + React Testing Library with TypeScript
- **Architecture:** Component composition, custom hooks

**Time Allocation:** 1-2 hours/day (parallel with DSA evening routine)

---

## 🎯 **PRIORITY 4: System Design (Weeks 5-8)**

### **Week 5-6: Fundamentals**
- **Scalability:** Load balancing, caching, database scaling
- **System Design Framework:** Requirements → Design → Scale
- **Practice Problems:** URL shortener, chat app, file storage

### **Week 7-8: Interview Prep**
- **Mock Interviews:** System design + coding rounds
- **Amazon-Specific:** Scalability questions, distributed systems
- **Portfolio Update:** Document your architecture decisions

**Time Allocation:** 3-4 hours/weekend

---

## 🔥 **Quick Assessment Recovery Strategy**

### **Next Amazon Assessment Preparation (2-3 weeks)**
Based on your recent experience, focus on these patterns first:

1. **Two Pointers** (Week 1) - Master these 5 problems:
   - Two Sum II (167)
   - Container With Most Water (11)
   - 3Sum (15)
   - Remove Duplicates from Sorted Array (26)
   - Valid Palindrome (125)

2. **Sliding Window** (Week 1) - Master these 5 problems:
   - Maximum Average Subarray I (643)
   - Longest Substring Without Repeating Characters (3)
   - Minimum Window Substring (76)
   - Permutation in String (567)
   - Sliding Window Maximum (239)

3. **Tree Traversal** (Week 2) - Master these 5 problems:
   - Binary Tree Inorder Traversal (94)
   - Maximum Depth of Binary Tree (104)
   - Binary Tree Level Order Traversal (102)
   - Binary Tree Right Side View (199)
   - Validate Binary Search Tree (98)

### **Amazon Assessment Tips:**
- **Time Management:** 45-60 minutes per problem typically
- **Test Cases:** Always test edge cases (empty arrays, single elements)
- **Code Quality:** Clean, readable code with good variable names
- **Communication:** Think out loud during virtual interviews

---

## 📈 **Progress Tracking**

### **Week 1 Goals:**
- [ ] Complete Two Pointers pattern (5 problems)
- [ ] Complete Sliding Window pattern (5 problems)
- [ ] Set up CI/CD pipeline for one project
- [ ] Start TypeScript basics course

### **Week 2 Goals:**
- [ ] Complete Fast & Slow Pointers pattern (4 problems)
- [ ] Complete Tree Traversal pattern (6 problems)
- [ ] Migrate one project to PostgreSQL
- [ ] Practice 10 mixed problems from Week 1 patterns

### **Week 4 Goals:**
- [ ] Complete Binary Search pattern (5 problems)
- [ ] Complete Graph Traversal pattern (5 problems)
- [ ] Finish AWS setup with monitoring
- [ ] Convert React project to TypeScript

### **Week 8 Goals:**
- [ ] Master all 15 patterns with 3+ problems each
- [ ] Complete 5 system design problems
- [ ] Finish TypeScript + React advanced concepts
- [ ] Complete 3 mock interviews
- [ ] Apply to 10+ senior full-stack positions

---

## 💡 **Study Resources - Integrated Approach**

### **Primary Resources:**
1. **Udemy Course (Weeks 1-2):** "Master the Coding Interview" - Foundation & Communication
2. **LeetCode Premium:** Pattern-based practice + Amazon-tagged problems
3. **Supplementary Pattern Recognition:** "14 Patterns to Ace Any Coding Interview" (free article)

### **Communication Practice:**
- **Course Exercises:** Complete all Udemy course exercises while explaining out loud
- **Mock Interviews:** Pramp, InterviewBit, AlgoExpert (after Week 2)
- **Recording Practice:** Record yourself solving problems to improve communication

### **Recommended Video Resources (High Quality Solutions):**

**For Priority Assessment Revenge Patterns:**
- **NeetCode (YouTube):** Longest Increasing Subsequence, Range Sum Query problems
- **William Fiset:** Segment Tree series (best explanations for range problems)
- **Back To Back SWE:** Number of Distinct Subsequences, advanced DP
- **Tushar Roy:** Complex DP sequence problems, great for subsequences

**For General Pattern Learning:**
- **NeetCode:** Most LeetCode patterns with clean explanations
- **Tech Interview Pro:** Pattern-based approach with communication tips
- **Kevin Naughton Jr.:** Good for seeing multiple approaches to same problem

**Learning Approach per Problem:**
1. **Search YouTube:** "[Problem Name] explanation" or "NeetCode [Problem Name]"
2. **Watch 1-2 videos** to see different approaches
3. **Close browser** and implement from memory
4. **Think out loud** while coding (practice interview communication)
5. **Test with examples** and handle edge cases yourself

### **Amazon-Specific Preparation:**
- **LeetCode:** Filter by Amazon tag + patterns learned
- **Interview Experiences:** Glassdoor Amazon SDE interviews
- **System Design:** Grokking the System Design Interview (if time allows)

---

## 🎯 **Assessment: Is Udemy Course + Practice Enough?**

### **Strengths of Your Udemy Course:**
- **Solid Foundation:** Covers all fundamental data structures
- **Communication Framework:** Teaches how to explain your approach
- **Interview Mindset:** Focuses on problem-solving process
- **Practical Examples:** Real coding interview scenarios

### **What You'll Need to Supplement:**
- **Pattern Recognition:** The course teaches data structures, but FAANG interviews test pattern recognition
- **Advanced Techniques:** Some patterns like "Monotonic Stack" or "Union Find" may not be covered
- **Speed & Efficiency:** Need more volume of practice problems
- **Amazon-Specific Problems:** Course is general, not company-specific

### **Recommendation: Course + Supplements**
**The Udemy course is perfect for your foundation (Weeks 1-2), but add these supplements:**

1. **Pattern Recognition (Week 3+):** Use the 15 patterns I listed as a checklist
2. **Volume Practice:** 200+ problems across patterns (course alone won't give you this)
3. **Amazon Focus:** Filter LeetCode by Amazon tag for company-specific practice
4. **Advanced Patterns:** YouTube/articles for patterns not covered in course

---

## 📋 **Updated Progress Tracking**

### **Week 1-2 Goals (Udemy Course Foundation):**
- [ ] Complete all Udemy course sections
- [ ] Solve all course practice problems while explaining approach
- [ ] Take detailed notes on each data structure's use cases
- [ ] Practice explaining "why" you chose specific approaches
- [ ] Complete 20+ easy LeetCode problems using course knowledge

### **Week 3-4 Goals (Pattern Recognition):**
- [ ] Master Two Pointers pattern (5 problems)
- [ ] Master Sliding Window pattern (5 problems)
- [ ] Master Fast & Slow Pointers pattern (4 problems)
- [ ] Complete 30+ medium problems using patterns
- [ ] Practice explaining algorithm choices in mock interviews

### **Week 5-6 Goals (Tree/Graph Mastery):**
- [ ] Master Tree Traversal patterns (6 problems)
- [ ] Master Binary Search pattern (5 problems)
- [ ] Master Graph Traversal patterns (5 problems)
- [ ] Complete 40+ medium problems across all patterns learned
- [ ] Record yourself solving 10 problems to improve communication

### **Week 7-8 Goals (Advanced Patterns):**
- [ ] Master Dynamic Programming pattern (6 problems)
- [ ] Master Backtracking pattern (4 problems)
- [ ] Master Heap/Priority Queue pattern (4 problems)
- [ ] Complete 50+ problems including hard difficulty
- [ ] Complete 5 timed mock interviews
- [ ] Apply to Amazon and other FAANG companies

---

## 🎯 **Key Success Metrics**

### **Technical Skills:**
- **DSA:** Solve 100+ problems across 15 patterns
- **System Design:** Complete 10+ design problems
- **Full-Stack:** Production-ready projects with TypeScript

### **Interview Readiness:**
- **Speed:** Solve medium problems in 30-45 minutes
- **Accuracy:** 80%+ success rate on practiced patterns
- **Communication:** Explain thought process clearly

### **Market Positioning:**
- **Portfolio:** 3+ production projects with modern tech stack
- **Experience:** Quantified impact from your current role
- **Salary Target:** $100k+ based on senior full-stack market rates

**Remember:** Your domain expertise is a huge advantage. The goal is to add the technical interview skills that FAANG companies test for, while leveraging your real-world experience.
