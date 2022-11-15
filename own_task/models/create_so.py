from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class CreateSo(models.Model):
    _name = "create.so"
    _rec_name="partner_id"

    get_state=fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('cancel', 'Cancelled'),
        ],string="Select State")

    product_ids=fields.Many2many(comodel_name="product.product",string="Select Products")
    partner_id=fields.Many2one(comodel_name="res.partner",string="Select Partner")
    my_sequence=fields.Char(string="Sequence" ,copy=False,required=True,readonly=True, default=lambda self: _('New'))

    def action_create_so(self):
        print("_________________________________",self)
        for record in self:
            lines=[]
            print("_________recs",record.partner_id.name)
            new_so=self.env['sale.order'].new(
                {   
                'partner_id':record.partner_id,
                'state':record.get_state,
                })
            new_so.onchange_partner_id()
            values = new_so._convert_to_write(new_so._cache)
            so_rec = self.env['sale.order'].create(values)
            print("_________recs",record.product_ids)
            for product in record.product_ids:
                print("______________________",product.id)
                a=lines.append((0,0,{'product_id':product.id}))
            print("aaaaaaaaaaaaaaaaaaaaaaaaaa",lines)
            so_rec.write({
                'order_line':lines
            })    

    @api.model
    def create(self, vals):
       if vals.get('my_sequence', _('New')) == _('New'):
           vals['my_sequence'] = self.env['ir.sequence'].next_by_code(
               'create.so') or _('New')
       res = super(CreateSo, self).create(vals)
       return res


class ResPartner(models.Model):   
    _inherit = 'res.partner'  
# This IS NAME SEARCH EXAMPLE


    @api.model   
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):        
        args = list(args or [])       
        if name :         
            args += ['|', '|' , ('name', operator, name), ('email', operator, name),('phone', operator, name)]   
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)


# THIS IS NAME GET EXAMPLE

    def name_get(self):
        result=[]
        for rec in self:
            print("____________________",rec)
            result.append((rec.id,'%s + %s' %(rec.name,rec.phone)))
        print("______________resutl",result)    
        return result                       



    