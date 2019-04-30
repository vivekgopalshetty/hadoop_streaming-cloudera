<h3># hadoop_streaming-cloudera
Its a simple map reduce program on cloudera using hadoop ecosystem

Dataset source:https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present-Dashboard/5cd6-ry5g

what is this project:
Based on Time of Crime – Analysis and predictions will be based on time of crimes i.e. which time have the maximum crime rates
and needs to be inspected more efficiently. 

Software/Hardware Requirements:
Tools used for this project:

<ul>
  <li>VMware Virtual Workstation</li>
  <li>Windows and Cloudera OS</li>
  <li>Hadoop HDFS</li>
  <li> Python</li>
  <li>Microsoft Excel </li>
</ul>

<strong>How does mapper and reducer helps analysis:</strong>

TIME BASED
The mapper functions used in this module uses the time at which the crime is registered. The hour component of the time 
is extracted and divided into 8 time slots and forwarded to the reducer where further analysis takes place.
The function links each line to its hour component and the reducer function counts the occurrence of each crime in every  
time slot displays the results time slot wise with numbers associated with each crime

<strong>conclusion:</strong>
Hence, I have made a project which helps to analyse the crimes based on time.Suggestions are provided on what policing practice should 
be implemented based on what crime is taking place according to the time.
you can also do it based on loctaion,district and also combine mutiple attributes to find better results

