<h3>SETTING UP OF ENVIRONMENT:</h3>

<b>LOCAL EXECUTION</b>
<ol>
<li>Create a file named project on desktop.</li>
<li>Add dataset,mapper file,and reducer file to it.</li>
<li>open cmd and check if code is working locally,if not make required changes.</li>
</ol>

<b>Hadoop execution</b>
<ol>
<li>copy your dataset as .txt file to hadoop HDFS</li>
<li>execute mapper and reducer using hadoop streaming jar</li>
</ol>

LOCAL EXECUTION  COMMANDS USED:

cd Desktop/project
cat crimedata_afterprep.txt | python time_map.py | python
time_reduce.py 

HADOOP EXECUTION COMMANDS USED:

copying file to hdfs:
hdfs dfs copyFromLocal /Desktop/project/ /user/mydata

command to execute jar:
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.13.0.jar \
-Dmapred.reduce.tasks=1 \
-input /user/big12/crimedata_afterprep.txt \
-file Desktop/project/district_map.py Desktop/project/district_reduce.py \
-mapper "python time_map.py" \
-reducer "python time_reduce.py" \
-output /user/time_output/output 

