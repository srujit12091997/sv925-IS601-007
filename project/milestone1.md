<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Srujit Varasala (sv925)</td></tr>
<tr><td> <em>Generated: </em> 12/13/2023 7:29:00 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/sv925" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T22.02.54image.png.webp?alt=media&token=c9e40b7e-3c80-4ac9-b53b-c704dc19449a"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of email invalid<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T22.03.29image.png.webp?alt=media&token=a5d29562-cbeb-4b3c-8beb-6d40bcaecdcd"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot for password not match<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T22.40.14image.png.webp?alt=media&token=02e06958-2452-41cc-a3da-bae4fcd9f6af"/></td></tr>
<tr><td> <em>Caption:</em> <p>valid data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T22.37.11image.png.webp?alt=media&token=c13e6675-dcaf-4f23-a620-c84b7a7da009"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of registration form<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T22.56.21image.png.webp?alt=media&token=15ac0026-f897-407c-abc0-b50c3b8c277f"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots of valid emails in the data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/srujit12091997/sv925-IS601-007/pull/26">https://github.com/srujit12091997/sv925-IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>The registration form utilizes a secure POST method for submitting user</div><div>data with fields<br>for username, email, password, and confirmation.&nbsp;</div><div><br></div><div>Backend SQL operations</div><div>handle validation, ensuring unique usernames and<br>emails, valid email formats, and password criteria</div><div>adherence.</div><div>Passwords undergo hashing before SQL insertion to<br>enhance security.&nbsp;</div><div>The database interactions involve secure</div><div>insertions using parameterized queries or other SQL injection<br>prevention methods.&nbsp;</div><div>While frontend validation isn't</div><div>explicitly detailed, backend SQL processes prioritize data security and<br>integrity.&nbsp;</div><div>The registration process underscores</div><div>SQL best practices for secure user information storage and validation,<br>contributing to a</div><div>seamless and protected user registration experience.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T23.01.32image.png.webp?alt=media&token=a2636ce8-5553-4be4-9d67-2817d0aa826b"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot for invalid user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T23.02.54image.png.webp?alt=media&token=25c085c8-7313-4d7b-a58f-6bebf7e90724"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot for mismatch user validation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T23.11.38image.png.webp?alt=media&token=4a0966ba-0782-42d4-92d3-7ce0cd441331"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for flask welcome message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/srujit12091997/sv925-IS601-007/pull/26">https://github.com/srujit12091997/sv925-IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>The registration form utilizes a secure POST method for submitting user data with</div><div>fields<br>for username, email, password, and confirmation.&nbsp;</div><div><br></div><div>Backend SQL operations handle validation, ensuring unique</div><div>usernames and<br>emails, valid email formats, and password criteria adherence.</div><div>Passwords undergo hashing before</div><div>SQL insertion to<br>enhance security.&nbsp;</div><div>The database interactions involve secure insertions using parameterized queries</div><div>or other SQL injection<br>prevention methods.&nbsp;</div><div>While frontend validation isn't explicitly detailed, backend SQL</div><div>processes prioritize data security and<br>integrity.&nbsp;</div><div>The registration process underscores SQL best practices for</div><div>secure user information storage and validation,<br>contributing to a seamless and protected user</div><div>registration experience.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T23.13.04image.png.webp?alt=media&token=7b9c5c7a-6b96-46ca-8f7d-e61bfb90f5d6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of successful logged off<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T23.14.57image.png.webp?alt=media&token=b15d1d8e-f938-4c93-a175-0bda68ce076c"/></td></tr>
<tr><td> <em>Caption:</em> <p>unable to login while logout<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/srujit12091997/sv925-IS601-007/pull/26">https://github.com/srujit12091997/sv925-IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>Session logic in a login system involves several steps to ensure</div><div>secure user authentication<br>and controlled access to protected pages. When a user logs</div><div>in, their credentials are<br>verified, and upon success, a unique session identifier is</div><div>generated. This identifier is stored,<br>either as a cookie in the user's browser</div><div>or on the server-side, marking the<br>user as authenticated. Protected pages, like a</div><div>dashboard, are configured to be accessible only<br>to users with valid sessions.</div><div><br></div><div>When a user attempts to access a login-protected page,<br>the server</div><div>checks for a valid session. If the session is absent or has<br>expired,</div><div>the user is redirected to the login page, preventing unauthorized access. The session</div><div>is<br>typically managed with a timeout to enhance security. When a user logs</div><div>out, the<br>session identifier is invalidated, ensuring the user loses access to protected</div><div>content.</div><div><br></div><div>The logic involves<br>verifying credentials, creating and managing sessions,</div><div>and checking for session validity when accessing protected<br>pages. This session-based approach enhances</div><div>user security, offering a seamless experience where only authenticated<br>users can access designated</div><div>content, effectively demonstrating that a logged-out user cannot reach login-protected<br>pages.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T23.16.55image.png.webp?alt=media&token=4208773f-32ad-464d-82d1-7d0a4f657b9b"/></td></tr>
<tr><td> <em>Caption:</em> <p>unable to login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T23.17.22image.png.webp?alt=media&token=963a483a-34b9-42a5-90be-fca11e2e89ba"/></td></tr>
<tr><td> <em>Caption:</em> <p>permission denied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T23.18.36image.png.webp?alt=media&token=e370d1d9-fcc9-497a-a8cf-6205470170d9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin record<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T23.19.16image.png.webp?alt=media&token=ed5daf4a-7308-471e-9eb2-2a4388f5a5dd"/></td></tr>
<tr><td> <em>Caption:</em> <p>created and modified<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/srujit12091997/sv925-IS601-007/pull/26">https://github.com/srujit12091997/sv925-IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>In the context of login-protected pages, the process typically involves a</div><div>server-side framework and<br>utilizes session management for user authentication. When a user logs in,</div><div>their credentials are<br>authenticated, and a unique session identifier is generated, associating the</div><div>user with a valid<br>session. This session identifier is stored, either as a</div><div>cookie on the user's browser<br>or on the server side.</div><div><br></div><div>Login-protected</div><div>pages are configured to check for the presence of<br>a valid session when</div><div>a user attempts to access them. The server-side logic verifies<br>if the user</div><div>has an active session; if not, the user is redirected to<br>the login</div><div>page. This mechanism ensures that only authenticated users with valid sessions can<br>access</div><div>protected content.</div><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>Role-protected pages in web applications establish controlled access based on user</div><div>roles or authorization<br>levels.&nbsp;</div><div><br></div><div>This process involves assigning roles during user creation</div><div>or updates, designating specific privileges to<br>roles like "admin" or "user."&nbsp;</div><div>When</div><div>users attempt to access role-protected pages, the server-side logic<br>verifies their assigned role,</div><div>ensuring appropriate authorization.</div><div>We use SQL tables in our database to<br>assign</div><div>roles to these users and once successful done, we can confirm roles of<br>each</div><div>user and give them permission likewise.&nbsp;</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T23.21.50image.png.webp?alt=media&token=8659d708-50d8-4038-8623-b18beba46a8e"/></td></tr>
<tr><td> <em>Caption:</em> <p>profile<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T23.22.56image.png.webp?alt=media&token=637c360c-3ad3-48e4-aa7d-b015e1deda01"/></td></tr>
<tr><td> <em>Caption:</em> <p>roles<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T23.24.35image.png.webp?alt=media&token=39c37016-ba76-4dd9-a22f-52be9eb756df"/></td></tr>
<tr><td> <em>Caption:</em> <p>sample<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T23.24.56image.png.webp?alt=media&token=d71a8117-9286-4fa2-ab14-e9fb475b56f9"/></td></tr>
<tr><td> <em>Caption:</em> <p>admin data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/srujit12091997/sv925-IS601-007/pull/26">https://github.com/srujit12091997/sv925-IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <div>We used following concepts of CSS&nbsp; to make look our website stylish and</div><div>cool</div><div><br></div><div>Selectors:<br>Define which HTML elements the styles should apply to.</div><div>Properties: Specify the visual attributes<br>of selected elements (e.g., color, font-size, margin).</div><div>Values: Assign specific values to properties, determining<br>the appearance of the selected elements.</div><div>&lt;span</div><div>style="font-size: 14px;"&gt;Selectors Hierarchy: Establish a hierarchy for styling,<br>enabling the cascading nature of</div><div>CSS, where styles can be inherited and overridden.</div><div>CSS allows<br>for the</div><div>creation of responsive designs, ensuring that web content adapts to different screen<br>sizes</div><div>and devices. It plays a crucial role in enhancing the user experience by</div><div>creating<br>visually appealing and well-organized web interfaces. CSS rules can be written directly</div><div>in HTML<br>files or kept in separate stylesheet files for better maintainability and</div><div>reusability.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T23.26.27image.png.webp?alt=media&token=f9607e92-b914-4b3d-a735-0a330985c770"/></td></tr>
<tr><td> <em>Caption:</em> <p>error password msg<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T23.27.17image.png.webp?alt=media&token=69431980-e6e8-456a-bbd9-18ce7333ce40"/></td></tr>
<tr><td> <em>Caption:</em> <p>login error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-12-13T23.28.47image.png.webp?alt=media&token=f7bbbb1c-ea57-4b1c-90c1-003613970f4c"/></td></tr>
<tr><td> <em>Caption:</em> <p>error<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/srujit12091997/sv925-IS601-007/pull/26">https://github.com/srujit12091997/sv925-IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <div>User-friendly messages are crafted for clarity and conciseness, ensuring easy comprehension.&nbsp;</div><div>Consistent use of</div><div>positive<br>language, maintaining context awareness, and effective error handling contribute to a positive</div><div>user experience.&nbsp;</div><div>Messages<br>also offer user assistance, such as relevant links or support details,</div><div>for additional information<br>or help when needed.&nbsp;</div><div>Prioritizing these elements enhances the overall usability</div><div>and user-friendliness of the<br>interface or application.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td>Not provided</td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <div>User data retrieval and display involve direct fetching from an SQL</div><div>table.</div><div><br></div><div>&nbsp;The backend initiates<br>an SQL query, such as SELECT username, email</div><div>FROM users WHERE user_id = ?,<br>retrieving the user's username and email.&nbsp;</div><div>The obtained data is then passed to the<br>template as variables, like return</div><div>render_template('profile.html', username=user_data['username'], email=user_data['email']).&nbsp;</div><div>Within the template, {{ render_field(form.username) }} and<br>{{ render_field(form.email)</div><div>}} statements dynamically fill the form fields with the user's current username<br>and</div><div>email.&nbsp;</div><div>This seamless integration allows users to view their existing information when</div><div>accessing the profile<br>page, creating a user-friendly experience for modifying and updating their</div><div>profile details.&nbsp;</div><div>The backend process<br>ensures efficient data retrieval, fostering a personalized</div><div>and responsive interface for users interacting with<br>their profile information.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> <p>captions<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/srujit12091997/sv925-IS601-007/pull/26">https://github.com/srujit12091997/sv925-IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <div>When a user successfully edits their profile, the backend logic manages</div><div>the update of<br>email, username, and password, incorporating validation measures.&nbsp;</div><div><br></div><div>Upon form</div><div>submission, the backend validates the data,<br>checking email format, ensuring username and email</div><div>uniqueness, and verifying password security.&nbsp;</div><div>If validation passes,<br>the backend updates the</div><div>corresponding records in the database, employing security measures like password<br>hashing.&nbsp;</div><div>The</div><div>user receives a success message upon a successful update, while validation failures prompt</div><div>appropriate<br>error messages.</div><div>In cases where sensitive information like passwords is updated,</div><div>the session may be<br>revalidated.&nbsp;</div><div>This comprehensive approach ensures a secure and</div><div>validated process for users, maintaining the integrity<br>and security of their profile information.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>I learned how to make different HTML and CSS files. How to make</div><div>register<br>and login pages.</div><div><br></div><div>How to make different SQL tables and give roles to</div><div>different users<br>according to SQL table entries.</div><div>i also learned how to utilize different&nbsp;</div><div>packages of flask<br>and everything.</div><div>I faced difficulties in following ways:</div><div>1. I was not</div><div>able to give roles<br>and apply correctly.</div><div>2. I was not able to use</div><div>CSS styling efficiently.</div><div>3. I was<br>not able to user Heroku app .yml files</div><div>updates.</div><div>With the help of class files<br>and professor i was able to correct</div><div>all my errors and succeed in completion<br>of this Assignment.</div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sv925-prod-9774fca88.herokuapp.com/login">https://is601-sv925-prod-9774fca88.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/sv925" target="_blank">Grading</a></td></tr></table>
