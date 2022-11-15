from odoo import fields, models,api,_

class Myclass(models.Model):
	_inherit="res.company"


	my=fields.Char(string="My Field")



class ResConfigSettings(models.TransientModel):
	_inherit="res.config.settings"

	my_field=fields.Char(related="company_id.my",string="My field",readonly=False)



class Sale(models.Model):
	_inherit="sale.order"

	def action_confirm(self):
		print("____________________",self.env.user.company_id.my)
		return super(Sale,self).action_confirm()		