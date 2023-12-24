<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Pumpkins</td></tr>
<tr><td> <em>Student: </em> Srujit Varasala (sv925)</td></tr>
<tr><td> <em>Generated: </em> 10/23/2023 11:22:01 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-2-pumpkins/grade/sv925" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/bb0d25257414c7154267baf0931dbef4">https://gist.github.com/MattToegel/bb0d25257414c7154267baf0931dbef4</a></li><li>Put them into a subfolder in your repository folder (I called my folder MP2)</li><li>Create a test folder as a subdirectory of MP2</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the below input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-24T01.36.55image.png.webp?alt=media&token=f589c01a-1a75-4da2-9447-127fca4bf66e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Snippet to calculate the cost of the pumpkin with UCID and date mentioned<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-24T01.38.44image.png.webp?alt=media&token=32670274-904f-4bbd-8935-70d1ce7d0535"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output of the pumpkin cost<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>The code initializes a variable named <code>total_cost</code> with an initial value of zero.<br>This variable is used to accumulate the total cost of the items in<br>the <code>inprogress_pumpkin</code> list by iterating through them with a for loop. This process<br>calculates the overall cost of the user&#39;s customized pumpkin order, including handling cents.<br>During the payment stage, the total cost is formatted as &quot;$ xx.xx,&quot; ensuring<br>that it includes up to two decimal places to represent the cents accurately.<br>In the above code, the pumpkin cost will be&nbsp;<span style="font-size: 16px; letter-spacing: 0.14992px;">calculated<br>accordingly after formatting.</span><br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-24T02.31.27image.png.webp?alt=media&token=473eae58-70b4-496d-9af3-efa0b1ed9ba6"/></td></tr>
<tr><td> <em>Caption:</em> <p>A full exception handling from OutOfStock, NeedsCleaningException and InvalidChoiceException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-24T02.32.05image.png.webp?alt=media&token=fcf6885a-a785-40b4-bb84-a5da47102683"/></td></tr>
<tr><td> <em>Caption:</em> <p>A Full exception handling code for ExceedRemaining, and InvalidPaymentException<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <p>These exceptions help handle various scenarios in the PumpkinMachine code.<div>1. OutOfStockException: Raised when<br>an item is out of stock, informing the user about the unavailability of<br>a specific item</div><div>2. NeedsCleaningException: Indicates that the machine needs cleaning and prompts the<br>user for action (clean or continue).</div><div>3.&nbsp;InvalidChoiceException: Signifies that an invalid choice was made<br>for the current stage, providing details of the error.</div><div>4.&nbsp;ExceededRemainingChoicesException: Occurs when the maximum<br>allowable choices for a category or stage have been exceeded.</div><div>5. InvalidPaymentException: Raised when<br>the user&#39;s payment amount doesn&#39;t match the expected total, prompting for a correct<br>payment</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-24T02.40.01image.png.webp?alt=media&token=18ca783c-bfb8-4266-8965-5ccd1b9ed6db"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is a snippet for first selection, face stencils and extra in stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-24T02.41.35image.png.webp?alt=media&token=6256e2c9-be50-4543-9432-894f0c575c88"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is a snippet for  3 face stencils adn 3 extra combo<br><br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-24T02.43.19image.png.webp?alt=media&token=36ff1514-8ec9-4a56-ba87-219d62e3efc2"/></td></tr>
<tr><td> <em>Caption:</em> <p>snippet for calculating cost of the pumpkin<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <div>1. `test_pumpkin_first_selection`: This test checks that you have to choose a pumpkin first.<br>If you try to pick a face stencil before a pumpkin, it will<br>stop you and say you're doing it wrong.<br></div><div><br></div><div>2. `test_face_stencils_in_stock`: This test makes sure<br>you can only add face stencils that are available. If you try to<br>add one that's not in stock, it will tell you it's out of<br>stock.</div><div><br></div><div>3. `test_extras_in_stock`: This test checks that you can only add extras that are<br>available. If you try to add one that's out of stock, it will<br>say it's not available.</div><div><br></div><div>4. `test_max_face_stencils`: This test makes sure you can add up<br>to three face stencils in any way you like. If you try to<br>add more than three, it will stop you and say you're adding too<br>many.</div><div><br></div><div>5. `test_max_extras`: This test verifies that you can add up to three extras<br>in any combination. If you try to add more than three, it will<br>tell you it's too many.</div><div><br></div><div>6. `test_calculate_cost`: This test checks if the cost is<br>calculated correctly based on your choices. It tries different combinations of pumpkins, face<br>stencils, and extras and compares the cost it calculates to the cost it<br>should be.</div><div><br></div><div>7. `test_total_sales`: This test ensures that the total cost of your purchases<br>is calculated properly. It makes two purchases and checks that the total cost<br>is zero because the correct payment hasn't been entered.</div><div><br></div><div>8. `test_total_products_increments`: This test checks<br>whether the number of products you've bought goes up correctly. It starts with<br>zero products, makes two purchases, and checks that it goes up to 2.</div><div><br></div><div>All<br>8 points are clearly mentioned for the code to follow the test cases<br>which is aligned with the code requirements for the test cases</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/srujit12091997/sv925-IS601-007/pull/18">https://github.com/srujit12091997/sv925-IS601-007/pull/18</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>I have learned about Enum language and its usage. Unit testing and clean<br>code. The things I lack are data validation, lack of testing incompletion where<br>unit tests are provided and they don&#39;t cover all the aspects of the<br>code.&nbsp;For comprehensive testing, additional scenarios should be considered.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-24T02.58.29image.png.webp?alt=media&token=aff7f42b-dd69-44a1-983d-88fe4405eeb3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for program execution of a different selection<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-24T03.02.13image.png.webp?alt=media&token=d4463f4d-08a1-4fe5-a7a0-bfd9eef84525"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for program execution of a different selection<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-24T03.03.53image.png.webp?alt=media&token=4ba11771-c385-409d-ab38-0c6cf2688474"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for program execution of a different selection<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-2-pumpkins/grade/sv925" target="_blank">Grading</a></td></tr></table>