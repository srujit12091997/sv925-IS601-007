<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Srujit Varasala (sv925)</td></tr>
<tr><td> <em>Generated: </em> 10/10/2023 12:07:00 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/sv925" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T01.00.06image.png.webp?alt=media&token=6a2a46f3-958b-43e8-afda-f06bf70e8656"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output message of the task was added<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T01.08.26image.png.webp?alt=media&token=d41c02ec-e120-4a06-a2d8-d6a28cfab9ca"/></td></tr>
<tr><td> <em>Caption:</em> <p>The snippet for adding the task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T01.13.24image.png.webp?alt=media&token=12498b13-74be-4696-ae2c-39969893e776"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output of showing the message successful<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T01.15.21image.png.webp?alt=media&token=4248fdf1-37bf-4db9-808b-7b70fbd2b05e"/></td></tr>
<tr><td> <em>Caption:</em> <p>error of the task updated tracking system<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <p>The process of addition of the task in the tracking system for each<br>mentioned item&#39;s solution requires the timestamp of the task to be completed at<br>a certain period of time which takes the input from the user and<br>the process time evaluation to complete the process of the task. In the<br>additional task, the name of the user and the description of the code<br>are given from the screenshots from the above task deliverables. save() function is<br>called in the update task such that the task is not lost and<br>saved in the following task deliverable<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T01.29.37image.png.webp?alt=media&token=7988e9a0-05bf-46bd-8b98-25302aa6d874"/></td></tr>
<tr><td> <em>Caption:</em> <p>This snippet is for updating the task if needed from the relevant attempt<br>of the task number <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <div>The purpose of the process update in the field is if the user<br>wants to update task 1 from addition to multiplication then the user may<br>change the same task slot 1 from addition to multiplication.</div>Code explanation: this function<br>is used to update the task; if a user wants to replace the<br>related task or the scenario of the task previously called in the update<br>task such that the task is not lost and saved in the following<br>task deliverable<br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T01.39.30image.png.webp?alt=media&token=f424e7b5-199e-4bb2-a4e3-12a5d9fad05a"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot has update task function displayed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T01.41.55image.png.webp?alt=media&token=e564cf09-6b1e-495e-b01d-9e37e76f0402"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot provides the output successful message of displaying and no changes in<br>the display is also applicable<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <p>the task is updated by the task indexing user has to give the<br>task number and the number is provided. The index is bound for a<br>valid indexing of the task data and it is provided from the date<br>time value.<div>The task requires the user to have the task index and ask<br>to describe the task and what the task does it will ask for<br>the task due and it will successfully update the task due and overwrites.<br>This helps the task to update the track delivered from the name of<br>the task to the date time of the task</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T02.07.10image.png.webp?alt=media&token=a248ecdd-ca98-4ce0-af1f-3bd65585d456"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot provided is the task done<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T02.09.16image.png.webp?alt=media&token=2e8f7294-d4f7-41c8-9ff6-157393daaa7d"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot provides the task 1 is completed <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T02.24.40image.png.webp?alt=media&token=7fe856e4-22e6-49ed-b6bb-241c120fe065"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for failure<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <p>Indexing is listed, The outbounds of the scenario and the task is delivered/done<br>will be known by checking the task for the done for the index<br>of the task. this will print the task that is already done or<br>the task that is just done by checking the task by index.<div>the function<br>prints a message indicating whether the task was updated or not.<br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T02.45.11image.png.webp?alt=media&token=555ae68d-0d2f-4d23-ae1a-2a71eb5d6eb0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for the task logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T02.47.04image.png.webp?alt=media&token=ad90c3a0-1df3-47b1-8cc7-291b3b0b0905"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of success and failure of the view task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T02.49.54image.png.webp?alt=media&token=4b27d3b7-a079-4576-9a75-c81ee4f221b0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Three tasks view screenshot<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T02.51.55image.png.webp?alt=media&token=23b91c8d-3342-41cc-a788-913ae79da83e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for the delete<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T02.53.19image.png.webp?alt=media&token=e4f5e322-0c09-42fb-ad29-5221930491d3"/></td></tr>
<tr><td> <em>Caption:</em> <p>delete screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <p>Indexing is listed, The outbounds of the scenario and the task is deleted<br>will be deleted once the task index is set to delete. This will<br>print the task that is already deleted or the task that it will<br>through up an error.<div>the function prints a message indicating whether the task was<br>updated or not.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T02.59.33image.png.webp?alt=media&token=59406505-db19-44f0-a5f5-1db8a1cfcc55"/></td></tr>
<tr><td> <em>Caption:</em> <p>incomplete tasks  will be provided<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T03.01.08image.png.webp?alt=media&token=6ff48d60-7383-48d2-a8e0-24d4b4d95a6a"/></td></tr>
<tr><td> <em>Caption:</em> <p>incomplete task outputs<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>The indexes will provide clear information on the tasks that are not completed<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T03.07.40image.png.webp?alt=media&token=ff809856-e781-44f4-b61d-22cb9aba63b4"/></td></tr>
<tr><td> <em>Caption:</em> <p>generates all the list of overdue tasks screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T03.09.20image.png.webp?alt=media&token=9ae972fb-168d-478e-a031-f918ae374fea"/></td></tr>
<tr><td> <em>Caption:</em> <p>overdue one task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>overdue is a task for which the item is clearly gives the task<br>indexes&nbsp; and the task name with the due time and the expiration time<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T03.13.09image.png.webp?alt=media&token=2b745be1-69ba-4335-836e-0f8ea4979b0c"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for time remaining<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T03.22.00image.png.webp?alt=media&token=d07182c6-7c7b-4dc0-95b2-707b1bbfa73e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success/failure of the time remaining screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <p>This time remaining function will provide each item be copied from the task<br>and will provided the indexes with task names and the timestamp.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T03.31.59image.png.webp?alt=media&token=80504dfe-69d2-4f32-b09b-c515f48d42d7"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots of the outputs of the codes<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T03.32.31image.png.webp?alt=media&token=ab2ae59f-afaa-412a-8da7-6236a95d4f47"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots of the outputs of the codes<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsv925%2F2023-10-10T03.34.35image.png.webp?alt=media&token=33ad6c88-937c-4ad5-9822-d8a9d786b676"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the JSON file opened in visual studios code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p>The code for the project is a task tracker for the task information<br>for add, view, update, delete, list, incomplete, overdue, help, exit, and done.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/srujit12091997/sv925-IS601-007/pull/8">https://github.com/srujit12091997/sv925-IS601-007/pull/8</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/sv925" target="_blank">Grading</a></td></tr></table>