from trytond.wizard import Wizard, StateView, StateTransition, Button , StateAction
from trytond.model import (ModelView, ModelSQL, MultiValueMixin, ValueMixin,
    DeactivableMixin, fields, Unique, sequence_ordered)
from trytond.pool import Pool
import xlsxwriter
import io
from trytond.report import Report

class CreateGSTR(ModelView):
    'GSTR1'
    __name__ = 'gstr1.export.report'

    from_date = fields.Date("From Date")
    to_date = fields.Date("To Date")



class GSTR1EXCEL(Report):
    __name__ = 'ir.model.gstr1'

    @classmethod
    def execute(cls, ids, data):
        
        pool = Pool()
        invoice = pool.get('account.invoice')
        date = pool.get('gstr1.export.report')
        # print("working "+ str(data['start_date'])) 
        Model = pool.get('ir.model')
        ActionReport = pool.get('ir.action.report')
        action_report_ids = ActionReport.search([
            ('report_name', '=', cls.__name__)
            ])

        Account.search([])
        
        if not action_report_ids:
            raise Exception('Error', 'Report (%s) not find!' % cls.__name__)
        action_report = ActionReport(action_report_ids[0])

        models = Model.browse(ids)  

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet()

        worksheet.write("A1","#")
        worksheet.set_column('A:A', 2)
        worksheet.write("B1","Invoice Number")
        worksheet.set_column('B:B', 16)
        worksheet.write("C1","Sales Data")
        worksheet.set_column('C:C', 16)
        worksheet.write("D1","Customer Name")
        worksheet.set_column('D:D', 16)
        worksheet.write("E1","GST Number")
        worksheet.set_column('E:E', 16)
        worksheet.write("F1","Rate")
        worksheet.set_column('F:F', 16)
        worksheet.write("G1","Discount Amount")
        worksheet.set_column('G:G', 16)
        worksheet.write("H1","GST")
        worksheet.set_column('H:H', 16)
        worksheet.write("I1","CGST")
        worksheet.set_column('I:I', 16)
        worksheet.write("J1","SGST")
        worksheet.set_column('J:J', 16)
        worksheet.write("K1","IGST")
        worksheet.set_column('K:K', 16)
        worksheet.write("L1","Round Off")
        worksheet.set_column('L:L', 16)
        worksheet.write("M1","Invoice Total")
        worksheet.set_column('M:M', 16)

        row = 1
        col = 0

        expenses = (
            [1 ,"SL/2021/02/0001","19-04-2021","Micheal","TAX123456","220660",0,"GST 18%",19859.4,19859.4,0,0.2,260379],
            [2 ,"SL/2021/02/0001","19-04-2021","Micheal","TAX123456","220660",0,"GST 18%",19859.4,19859.4,0,0.2,260379],
            [3 ,"SL/2021/02/0001","19-04-2021","Micheal","TAX123456","220660",0,"GST 18%",19859.4,19859.4,0,0.2,260379],
            [4 ,"SL/2021/02/0001","19-04-2021","Micheal","TAX123456","220660",0,"GST 18%",19859.4,19859.4,0,0.2,260379]

        )

        for i ,invoiceno,salesdate ,customer ,gstn,rate,discount,gst,cgst,sgst,igst,rof,invtot in (expenses):
            worksheet.write(row, col,     i)
            worksheet.write(row, col + 1, invoiceno)
            worksheet.write(row, col + 2, salesdate)
            worksheet.write(row, col + 3, customer)
            worksheet.write(row, col + 4, gstn)
            worksheet.write(row, col + 5, rate)
            worksheet.write(row, col + 6, discount)
            worksheet.write(row, col + 7, gst)
            worksheet.write(row, col + 8, cgst)
            worksheet.write(row, col + 9, sgst)
            worksheet.write(row, col + 10, igst)
            worksheet.write(row, col + 11, rof)
            worksheet.write(row, col + 12, invtot)
            row += 1
        
        workbook.close()
        output.seek(0)
        # output.close()
        
        return ('xlsx', output.read(), False, action_report.name)



class GSTR1Report(Wizard):
    'Export GSTR1'
    __name__ = "gstr1.create_report"

    start = StateView('gstr1.export.report',
        'gstr1.create_gstr1_report_start_view_form', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Generate', 'generate_report', 'tryton-ok', default=True),
            ])  
    
    generate_report = StateAction('gstr1.report_model_gstr1')


    def do_generate_report(self, action):
        
        from_date = self.start.from_date
        to_date = self.start.to_date


        return action , {
            'start_date': self.start.from_date,
            'end_date': self.start.to_date
        }




   

        
        
