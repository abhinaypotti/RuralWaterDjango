from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from .models import funddetails
from .models import revenuedetails
from .models import villages
# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'registration.html')

def registerihhl(request):
    return render(request,'regihhl.html')

def fundinputpage(request):
    return render(request,'fundinput.html')
def login(request):
    return render(request,'login.html')
def adminportal(request):
    return render(request,'adminportal.html')

def empreg(request):
    return render(request,'employeereg.html')

def filtrationunit(request):
    return render(request,'filtrationunit.html')

def quality(request):
    return render(request,'qualityassurance.html')

def sanction(request):
    return render(request,'sanction.html')

def villagereg(request):
    return render(request,'villagereg.html')

def waterrevenueinput(request):
    return render(request,'waterrevenueinput.html')

def waterrevenueoutput(request):
    return render(request, 'waterrevenue.html')

def pipeline(request):
    return render(request,'waterpipelineconnection.html')

def watersourcereg(request):
    return render(request,'watersource.html')

def reqwatercon(request):
    return render(request,'reqwatercon.html')

def reqihhl(request):
    return render(request,'reqihhl.html')

def funding(request):
    return render(request,'funding.html')




def employeereg(request):
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        database="ruralwatersupplydb")
        cursor = connection.cursor()

        postgres_insert_query = """INSERT INTO public."Employee_details"("Emp_id", "Emp_pwd", "Emp_type", "Emp_age") VALUES (%s, %s, %s, %s);"""
        val1 = int(request.GET['email'])
        val2 = request.GET['password']
        val3 = request.GET['emptype']
        val4 = request.GET['age']
        val5 = request.GET['salary']
        record_to_insert = (val1, val2,val3,val4)
        cursor.execute(postgres_insert_query, record_to_insert)
        postgres_insert_query = """INSERT INTO public."Employee_salary"("Emp_id", "Emp_type", "Emp_salary") VALUES (%s, %s, %s);"""
        record_to_insert = (val1,val3,val5)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


    return render(request,'adminportal.html')



def insertvillage(request):
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        database="ruralwatersupplydb")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO public."Village_Details"("Village_id", "Village_name", "District_name") VALUES (%s, %s, %s);"""
        val1 = int(request.GET['villageid'])
        val2 = request.GET['villagename']
        val3 = request.GET['districtname']
        record_to_insert = (val1, val2,val3)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


    return render(request,'adminportal.html')

def insertfiltration(request):
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        database="ruralwatersupplydb")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO public."Filtration_Details"("Filtration_id", "Filtration_location", "Filtration_capacity") VALUES (%s, %s, %s);"""
        val1 = int(request.GET['filtrationid'])
        val2 = request.GET['location']
        val3 = request.GET['method']
        val4 = request.GET['capacity']
        record_to_insert = (val1, val2,val4)
        cursor.execute(postgres_insert_query, record_to_insert)

        postgres_insert_query = """ INSERT INTO public."FiltrationMethod"("Filtration_id", "Filtration_method") VALUES (%s, %s); """
        record_to_insert = (val1,val3)

        cursor.execute(postgres_insert_query,record_to_insert)    

        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


    return render(request,'adminportal.html')


def insertquality(request):
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        database="ruralwatersupplydb")
        cursor = connection.cursor()

        postgres_insert_query = """INSERT INTO public."Quality_assurance"("Ref_id", "Chloride", "Flouride", "Arsenic", "Grade_of_contamination") VALUES (%s, %s, %s, %s, %s);"""
        val1 = int(request.GET['refid'])
        val2 = int(request.GET['chloride'])
        val3 = int(request.GET['arsenic'])
        val4 = int(request.GET['fluoride'])
        if(val2 > 50 and val3 > 50 and val4 > 50):
            val5 ='A'
        else:
            val5 = 'B'
        
        record_to_insert = (val1, val2,val4,val3,val5)
        cursor.execute(postgres_insert_query, record_to_insert)   

        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


    return render(request,'qualityassurance.html',{'grade':val5})


def insertsanction(request):
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        database="ruralwatersupplydb")
        cursor = connection.cursor()

        postgres_insert_query = """INSERT INTO public."Sanction"("Sanction_id", "Sanctioned_amount", "Year_of_sanction", "Completion_year") VALUES (%s, %s, %s, %s);"""
        val1 = int(request.GET['sanctionid'])
        val2 = int(request.GET['amount'])
        val3 = int(request.GET['year1'])
        val4 = int(request.GET['year2'])
    
        
        record_to_insert = (val1, val2,val3,val4)
        cursor.execute(postgres_insert_query, record_to_insert)   

        val5 = int(request.GET['worksid'])
        val6 = int(request.GET['maxtranspo'])
        
        postgres_insert_query = """ INSERT INTO public."Works"("Works_id", "Max_Transportation_of_water") VALUES (%s, %s); """
        record_to_insert = (val5, val6)
        cursor.execute(postgres_insert_query, record_to_insert)

        postgres_insert_query = """ INSERT INTO public."Deposit_Works"( "Sanction_id", deposit_works) VALUES (%s, %s); """
        record_to_insert = (val1, val5)
        cursor.execute(postgres_insert_query, record_to_insert)




        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")



    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


    return render(request,'adminportal.html')


def insertpipe(request):
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        database="ruralwatersupplydb")
        cursor = connection.cursor()

        postgres_insert_query = """INSERT INTO public."Pipeline_details"("Connection_id", "Length_of_pipeline", "Year_of_laying", "Pipe_type") VALUES (%s, %s, %s, %s);"""
        val1 = int(request.GET['connectionid'])
        val2 = int(request.GET['length'])
        val3 = int(request.GET['year'])
        val4 = request.GET['ptype']
    
        
        record_to_insert = (val1, val2,val3,val4)
        cursor.execute(postgres_insert_query, record_to_insert)   

        val5 = request.GET['ctype']
        val6 = int(request.GET['flatrate'])
        
        postgres_insert_query = """ INSERT INTO public."Water_Connection_Type"("Connection_id", "Connection_type", "Flat_rate") VALUES (%s, %s, %s); """
        record_to_insert = (val1,val5, val6)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


    return render(request,'adminportal.html')


def insertsource(request):
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        database="ruralwatersupplydb")
        cursor = connection.cursor()

        postgres_insert_query = """INSERT INTO public."Water_Source_Details"("Source_id", "Source_name", "Source_Capacity", "Maintenance_review_start_date", "Maintenance_review_end_date") VALUES (%s, %s, %s, %s, %s);"""
        val1 = int(request.GET['sourceid'])
        val2 = request.GET['sourcename']
        val3 = int(request.GET['sourcecapacity'])
        val4 = request.GET['date1']
        val5 = request.GET['date2']
        record_to_insert = (val1, val2,val3,val4,val5)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


    return render(request,'adminportal.html')


def userreg(request):
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        database="ruralwatersupplydb")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO public."Users"("User_id", "User_Password", "First_name", "Last_name", "Location_address", "Village_id") VALUES (%s, %s, %s, %s, %s, %s);"""
        val1 = int(request.GET['villageid'])
        val2 = request.GET['fname']
        val3 = request.GET['lname']
        val4 = request.GET['address']
        val5 = request.GET['password']
        val6 = request.GET['userid']

        record_to_insert = (val6, val5,val2,val3,val4,val1)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


    return render(request,'login.html')


def userlogin(request):
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        database="ruralwatersupplydb")
        cursor = connection.cursor()
        val1 = request.GET['email']
        val2 = request.GET['password']
        

        sql_select_Query = """SELECT "User_Password" FROM public."Users" where "User_id" ='""" + val1 +"""';"""
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            userpassword = row[0]
        
        


        connection.commit()
        count = cursor.rowcount
        if(userpassword == val2):
            return render(request,'userhome.html')
        print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


    return render(request,'login.html')

def newwaterconreq(request):
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        database="ruralwatersupplydb")
        cursor = connection.cursor()


        postgres_insert_query = """ INSERT INTO public."Requirements"( "Request_id", "Requirement_id", "Request_type") VALUES (%s, %s, %s);"""
        val1 = int(request.GET['requestid'])
        val2 = int(request.GET['requirementid'])
        val3 = 'Water Connection'
    
        record_to_insert = (val1,val2,val3)
        cursor.execute(postgres_insert_query, record_to_insert)

        postgres_insert_query = """ INSERT INTO public."Village_request"( "Request_id", "Requirement_id", "Village_id") VALUES (%s, %s, %s);"""
        val4 = int(request.GET['villageid'])
    
        record_to_insert = (val1,val2,val4)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


    return render(request,'reqwatercon.html')


def newihhlcon(request):
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        database="ruralwatersupplydb")
        cursor = connection.cursor()


        postgres_insert_query = """ INSERT INTO public."Requirements"( "Request_id", "Requirement_id", "Request_type") VALUES (%s, %s, %s);"""
        val1 = int(request.GET['requestid'])
        val2 = int(request.GET['requirementid'])
        val3 = 'Individual House Hold Latrine'
    
        record_to_insert = (val1,val2,val3)
        cursor.execute(postgres_insert_query, record_to_insert)

        postgres_insert_query = """ INSERT INTO public."Village_request"( "Request_id", "Requirement_id", "Village_id") VALUES (%s, %s, %s);"""
        val4 = int(request.GET['villageid'])
    
        record_to_insert = (val1,val2,val4)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


    return render(request,'reqihhl.html')

def fundretrieve(request):
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        database="ruralwatersupplydb")
        cursor = connection.cursor()
        list1 = []
        sql_select_Query = """SELECT "IHHL_fund_id", "Sanctioned_IHHL", "Estimated_cost", "Funds_from_ngo" FROM public."IHHL_expenditure_details";"""
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        i =1
        for row in records:
            x = funddetails()
            x.s = i
            x.IHHL_fund_id = row[0]
            x.Sanctioned_IHHL = row[1]
            x.Estimated_Cost = row[2]
            x.Funds_from_ngo = row[3]
            i = i + 1
            list1.append(x)

        


        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


    return render(request,'funding.html',{'funddetails': list1})


def insertfund(request):
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        database="ruralwatersupplydb")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO public."IHHL_expenditure_details"( "IHHL_fund_id", "Sanctioned_IHHL", "Estimated_cost", "Funds_from_ngo") VALUES (%s, %s, %s, %s);"""
        val1 = int(request.GET['ihhl_fund_id'])
        val2 = int(request.GET['sanctioned_ihhl'])
        val3 = int(request.GET['estimated_cost'])
        val4 = int(request.GET['funds_from_ngo'])
        

        record_to_insert = (val1, val2,val3,val4)
        cursor.execute(postgres_insert_query, record_to_insert)

        postgres_insert_query = """ INSERT INTO public."Village_IHHL"( "IHHL_id", "IHHL_fund_id", "Village_id") VALUES (%s, %s, %s);"""
        val5 = int(request.GET['villageid'])
        val6 = int(request.GET['ihhlid'])
        

        record_to_insert = (val6, val1,val5)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


    return render(request,'fundinput.html')


def insertwaterrevenue(request):
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        database="ruralwatersupplydb")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO public."Water_revenue_details"( "Bill_id", "Generated_funds") VALUES (%s, %s);"""
        val1 = int(request.GET['billid'])
        val2 = int(request.GET['amount'])

        record_to_insert = (val1, val2)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


    return render(request,'waterrevenueinput.html')

def waterrevenueretrieve(request):
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        database="ruralwatersupplydb")
        cursor = connection.cursor()
        list1 = []
        sql_select_Query = """SELECT "Bill_id", "Generated_funds" FROM public."Water_revenue_details";"""
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        i =1
        for row in records:
            x = revenuedetails()
            x.s = i
            x.billid = row[0]
            x.amount = row[1]
            i = i + 1
            list1.append(x)

        


        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


    return render(request,'waterrevenue.html',{'revenuedetails': list1})


def insertihhl(request):
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        database="ruralwatersupplydb")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO public."Individual_Household_Latrines"( "IHHL_id", "Inprogress_ihhl", "Completed_ihhl", "Sanctioned_amount") VALUES (%s, %s, %s, %s);"""
        val1 = int(request.GET['ihhlid'])
        val2 = int(request.GET['inprogressihhl'])
        val3 = int(request.GET['completedihhl'])
        val4 = int(request.GET['amount'])

        record_to_insert = (val1, val2, val3, val4)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


    return render(request,'regihhl.html')


def villageoutput(request):
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="1234",
                                        host="localhost",
                                        database="ruralwatersupplydb")
        cursor = connection.cursor()
        list1 = []
        sql_select_Query = """SELECT "Village_id", "Village_name", "District_name" FROM public."Village_Details";"""
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            x = villages()
            x.villageid = row[0]
            x.villagename = row[1]
            x.districtname = row[2]
            list1.append(x)

        


        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")




    return render(request,'villageoutput.html',{'villagedetails':list1})


















