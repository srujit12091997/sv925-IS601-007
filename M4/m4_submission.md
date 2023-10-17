<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Srujit Varasala (sv925)</td></tr>
<tr><td> <em>Generated: </em> 10/17/2023 4:18:47 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/sv925" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sub-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T01.05.23image.png.webp?alt=media&token=f6d7d9b3-2d34-4b3c-aff3-60447f4643c9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Addition code snippet<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T01.06.22image.png.webp?alt=media&token=18d58dad-2f81-4654-a99b-b48272ce0a9c"/></td></tr>
<tr><td> <em>Caption:</em> <p>valid solution for addition<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T01.08.58image.png.webp?alt=media&token=c93e4f3b-b499-4d31-ba03-ff36f934f881"/></td></tr>
<tr><td> <em>Caption:</em> <p>Subtraction code snippet<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T01.10.14image.png.webp?alt=media&token=a3d1f3a5-ceba-4bfd-9f9b-e7bec634a0a1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid solution for subtraction<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T01.18.39image.png.webp?alt=media&token=080520ad-55c7-468c-8d5e-9f6438403ccb"/></td></tr>
<tr><td> <em>Caption:</em> <p>Multiplication code snippet<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T01.11.37image.png.webp?alt=media&token=e644074f-a5c4-493b-857a-58e1e67ed73e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid solution for multiplication<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T01.13.30image.png.webp?alt=media&token=c22486fc-e9c9-4735-a37a-d922b76cb391"/></td></tr>
<tr><td> <em>Caption:</em> <p>Validating Solution for subtraction<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T01.19.11image.png.webp?alt=media&token=a6f8dc80-919c-4444-968f-d5aaa658016c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Multiplication code snippet<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T03.27.29image.png.webp?alt=media&token=83fd42ed-6407-4be3-8f84-cfc4faab6ff9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet for the passing number add number<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T03.31.33image.png.webp?alt=media&token=305035ae-449f-484d-9068-5dbf6486a3c3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T03.32.16image.png.webp?alt=media&token=24f3f184-e8d8-42df-99dc-e08df7267627"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T03.33.32image.png.webp?alt=media&token=2e0e9c48-705a-48d5-afd1-4c4f4ff000b5"/></td></tr>
<tr><td> <em>Caption:</em> <p>code snippet<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T03.34.16image.png.webp?alt=media&token=0defafe3-4967-4b4f-a144-148295393598"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code sippet<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T03.35.15image.png.webp?alt=media&token=0eea576e-65ce-46ef-ae30-5fdbd6b07328"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T03.35.49image.png.webp?alt=media&token=bc002513-3b88-4e29-9eb2-7e1a4fffeb93"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-sub-number snippet<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T03.36.18image.png.webp?alt=media&token=b988974b-a599-4b08-9551-86959514cb78"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T03.37.11image.png.webp?alt=media&token=d33fea61-9519-416c-aafb-8a4798756f43"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-mult-number  snippet<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T03.37.19image.png.webp?alt=media&token=09082316-e866-4d12-80b1-34a522bf0d5c"/></td></tr>
<tr><td> <em>Caption:</em> <p>test cases<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T03.38.07image.png.webp?alt=media&token=6fb1bf32-2c52-4a11-b311-c9013ea46dbd"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-multi-number snippet<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T03.38.16image.png.webp?alt=media&token=d7f2791a-184f-4352-ab00-b225bc5f79de"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T03.39.51image.png.webp?alt=media&token=f6e34d3a-26b7-4ce2-8abf-95d8aecf5b9f"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-div-number snippet<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T03.39.59image.png.webp?alt=media&token=1fc04a34-12cc-49d7-80e7-2bff3f95a090"/></td></tr>
<tr><td> <em>Caption:</em> <p>test output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T03.40.16image.png.webp?alt=media&token=4a94f4e4-4079-402e-bd8f-7858076d47c5"/></td></tr>
<tr><td> <em>Caption:</em> <p>test output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-17T03.41.17image.png.webp?alt=media&token=540e0cc3-a26c-4729-bf31-ab0c13000476"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-div-number<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>From this Assignment, I have learned to create a calculator for adding, subtracting,<br>multiplying, and dividing 2-digits using Python code. Writing the test cases for the<br>code to check the code that allows the assert keywords to verify a<br>condition in your code to produce an assertion error that compromises three cases<br>assigned to calculator.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment, specially include how fixtures and parameterized tests work</td></tr>
<tr><td> <em>Response:</em> <p>These test cases parameterized test cases assess the addition multiplication subtraction and division<br>of the functionalities of a calculator by evaluating various pairs of numbers. These<br>cases check the addition operation or calculator by evaluating the various input number<br>pairs the solution matches the result for different combination of positive and negative<br>number<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/srujit12091997/sv925-IS601-007/pull/14">https://github.com/srujit12091997/sv925-IS601-007/pull/14</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/sv925" target="_blank">Grading</a></td></tr></table>