/*Accumulo*/
CREATE TABLE Temp1 AS
SELECT DISTINCT SONAR_ISSUES.creationDate, SONAR_ISSUES.closeDate, SONAR_ISSUES.type, SONAR_ISSUES.component, SONAR_ISSUES.effort, SONAR_ISSUES.debt, SONAR_ISSUES.message, (CASE 
						WHEN SONAR_ISSUES.severity = 'INFO' THEN '0.1'
						WHEN SONAR_ISSUES.severity = 'MINOR' THEN '0.2'
						WHEN SONAR_ISSUES.severity = 'MAJOR' THEN '0.4'	
						WHEN SONAR_ISSUES.severity = 'CRITICAL' THEN '0.6'
						WHEN SONAR_ISSUES.severity = 'BLOCKER' THEN '0.8' 
					   END) as severity, 
                       (CASE 
						WHEN SONAR_MEASURES.sqaleRating = '5' THEN '0.05'
						WHEN SONAR_MEASURES.sqaleRating = '4' THEN '0.1'
					    WHEN SONAR_MEASURES.sqaleRating = '3' THEN '0.2'	
						WHEN SONAR_MEASURES.sqaleRating = '2' THEN '0.5'
						WHEN SONAR_MEASURES.sqaleRating = '1' THEN '1'
		  			   END) as maintainability_Rating,
                       (CASE 
						WHEN SONAR_MEASURES.securityRating = '5' THEN '0.05'
						WHEN SONAR_MEASURES.securityRating = '4' THEN '0.1'
					    WHEN SONAR_MEASURES.securityRating = '3' THEN '0.2'	
						WHEN SONAR_MEASURES.securityRating = '2' THEN '0.5'
						WHEN SONAR_MEASURES.securityRating = '1' THEN '1'
		  			   END) as security_Rating, 
                        (CASE 
						WHEN SONAR_MEASURES.reliabilityRating = '5' THEN '0.05'
						WHEN SONAR_MEASURES.reliabilityRating = '4' THEN '0.1'
					    WHEN SONAR_MEASURES.reliabilityRating = '3' THEN '0.2'	
						WHEN SONAR_MEASURES.reliabilityRating = '2' THEN '0.5'
						WHEN SONAR_MEASURES.reliabilityRating = '1' THEN '1'
		  			   END) as reliability_Rating, SONAR_MEASURES.developmentCost as development_cost
FROM SONAR_ISSUES, SONAR_MEASURES
WHERE SONAR_ISSUES.creationCommitHash = SONAR_MEASURES.commitHash AND SONAR_ISSUES.projectID = "accumulo"
ORDER BY SONAR_ISSUES.component, SONAR_ISSUES.creationDate, SONAR_ISSUES.message

/*Summarized Parameters*/
CREATE TABLE Temp1_res AS
SELECT Temp1.creationDate, Temp1.component, sum(Temp1.effort) AS totalEffort, avg(severity), avg(maintainability_Rating), avg(security_Rating), avg(reliability_Rating)
FROM Temp1
GROUP BY Temp1.creationDate, Temp1.component
ORDER BY Temp1.component, Temp1.creationDate

/*Getting the result*/
SELECT *
FROM Temp1_res
WHERE totalEffort > 0

/*Cocoon*/
CREATE TABLE Temp1 AS
SELECT DISTINCT SONAR_ISSUES.CREATION_DATE, SONAR_ISSUES.CLOSE_DATE, SONAR_ISSUES.TYPE, SONAR_ISSUES.COMPONENT, SONAR_ISSUES.EFFORT,  SONAR_ISSUES.DEBT, SONAR_ISSUES.MESSAGE,
                        (CASE 
						WHEN SONAR_ISSUES.SEVERITY = 'INFO' THEN '0.1'
						WHEN SONAR_ISSUES.SEVERITY = 'MINOR' THEN '0.2'
						WHEN SONAR_ISSUES.SEVERITY = 'MAJOR' THEN '0.4'	
						WHEN SONAR_ISSUES.SEVERITY = 'CRITICAL' THEN '0.6'
						WHEN SONAR_ISSUES.SEVERITY = 'BLOCKER' THEN '0.8' 
					   END) as SEVERITY, 
                       (CASE 
						WHEN SONAR_MEASURES.SQALE_RATING = '5' THEN '0.05'
						WHEN SONAR_MEASURES.SQALE_RATING = '4' THEN '0.1'
					    WHEN SONAR_MEASURES.SQALE_RATING = '3' THEN '0.2'	
						WHEN SONAR_MEASURES.SQALE_RATING = '2' THEN '0.5'
						WHEN SONAR_MEASURES.SQALE_RATING = '1' THEN '1'
		  			   END) as maintainability_Rating,
                       (CASE 
						WHEN SONAR_MEASURES.SECURITY_RATING = '5' THEN '0.05'
						WHEN SONAR_MEASURES.SECURITY_RATING = '4' THEN '0.1'
					    WHEN SONAR_MEASURES.SECURITY_RATING = '3' THEN '0.2'	
						WHEN SONAR_MEASURES.SECURITY_RATING = '2' THEN '0.5'
						WHEN SONAR_MEASURES.SECURITY_RATING = '1' THEN '1'
		  			   END) as security_Rating, 
                        (CASE 
						WHEN SONAR_MEASURES.RELIABILITY_RATING = '5' THEN '0.05'
						WHEN SONAR_MEASURES.RELIABILITY_RATING = '4' THEN '0.1'
					    WHEN SONAR_MEASURES.RELIABILITY_RATING = '3' THEN '0.2'	
						WHEN SONAR_MEASURES.RELIABILITY_RATING = '2' THEN '0.5'
						WHEN SONAR_MEASURES.RELIABILITY_RATING = '1' THEN '1'
		  			   END) as RELIABILITY_RATING, SONAR_MEASURES.DEVELOPMENT_COST as DEVELOPMENT_COST
FROM SONAR_ISSUES, SONAR_MEASURES
WHERE SONAR_ISSUES.CREATION_ANALYSIS_KEY = SONAR_MEASURES.ANALYSIS_KEY and SONAR_ISSUES.PROJECT_ID = "org.apache:cocoon"
ORDER BY COMPONENT, SONAR_ISSUES.MESSAGE, SONAR_ISSUES.CREATION_DATE

/*Summarized Parameters*/
CREATE TABLE Temp1_res AS
SELECT Temp1.CREATION_DATE, Temp1.COMPONENT, sum(Temp1.EFFORT) AS TOTAL_EFFORT, avg(severity), avg(maintainability_Rating), avg(security_Rating), avg(reliability_Rating)
FROM Temp1
WHERE TOTAL_EFFORT > 0
GROUP BY Temp1.CREATION_DATE, Temp1.COMPONENT
ORDER BY Temp1.COMPONENT, TEMP1.CREATION_DATE

/*Getting the result*/
SELECT *
FROM Temp1_res
WHERE TOTAL_EFFORT > 0