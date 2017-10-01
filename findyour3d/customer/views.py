import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView

from .models import Customer
from .forms import AddCustomerForm, AddAdvancedCustomerForm

logger = logging.getLogger(__name__)


class AddCustomerView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = AddCustomerForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            if self.request.user.user_type == 1:
                if self.request.user.customer_set.all():
                    if self.request.user.customer_set.first().is_advanced_filled:
                        return reverse('dashboard:company')
                    else:
                        return redirect('customers:advanced', self.request.user.customer_set.first().pk)
            else:
                return HttpResponseForbidden()
        return super(AddCustomerView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        f = form.save(commit=False)
        if f.material is not None and f.process is not None:
            f.is_advanced_filled = True
        f.save()
        return super().form_valid(form)

    def get_success_url(self):
        if self.object.material is not None and self.object.process is not None:
            return reverse('dashboard:company')
        else:
            return reverse('customers:advanced', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        return Customer.objects.get(user=self.request.user)

    def get_initial(self):
        initial_data = super(AddCustomerView, self).get_initial()
        initial_data['user'] = self.request.user
        return initial_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EditCustomerView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = AddCustomerForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            if self.request.user.user_type == 1:
                if int(self.kwargs['pk']) == request.user.customer_set.first().pk:
                        if not self.request.user.customer_set.all():
                            return redirect('customers:add')
                else:
                    raise PermissionDenied
            else:
                raise PermissionDenied
        return super(EditCustomerView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        f = form.save(commit=False)
        if f.material is not None and f.process is not None:
            f.is_advanced_filled = True
        f.save()
        return super().form_valid(form)

    def get_success_url(self):
        if self.object.material is not None and self.object.process is not None:
            return reverse('dashboard:company')
        else:
            return reverse('customers:advanced', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        return Customer.objects.get(id=self.kwargs['pk'])

    def get_initial(self):
        initial_data = super(EditCustomerView, self).get_initial()
        initial_data['user'] = self.request.user
        return initial_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_button'] = False
        if self.request.user.user_type == 1:
            if self.request.user.customer_set.all():
                if self.request.user.customer_set.first().is_advanced_filled:
                    context['back_button'] = True
        return context


class AddAdvancedCustomerView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = AddAdvancedCustomerForm
    template_name = 'customer/customer_advanced_form.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            if self.request.user.user_type == 1:
                if int(self.kwargs['pk']) == request.user.customer_set.first().pk:
                        # if self.request.user.customer_set.all():
                        #     if self.request.user.customer_set.first().is_advanced_filled:
                        #         return reverse('dashboard:company')
                        if not self.request.user.customer_set.all():
                            return redirect('customers:add')
                else:
                    raise PermissionDenied
            else:
                raise PermissionDenied
            return super(AddAdvancedCustomerView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        f = form.save(commit=False)
        f.is_advanced_filled = True
        f.save()

        if f.basic_material is not None:
            if f.basic_material == 1:  # metals
                if f.is_precious_metal == 2:
                    print('Silver / Gold (DMLS / SLM) Gold or Silver are obvious choices for things like jewelry '
                          'or trinkets that are ornate and luxurious. Their beauty and rarity come with at a '
                          'price, as they are both hard to print and are very expensive. They are printed via '
                          'Direct Metal Laser Sintering (DMLS) or Selective Laser Melting (SLM). This is ideal '
                          'for a project that stands above in beauty and is worth every penny.')
                    f.process = 1
                    f.material = 12
                elif f.is_precious_metal == 3:
                    if f.metal_concern == 1:  # Conductivity
                        print('Copper (SLM / DMLS) Copper is a commonly used conductive metal that is rather '
                              'inexpensive even to 3D Print. It offers good resistance to wear and can be polished '
                              'down to reveal rather ornate features, if required. Copper is printed using '
                              'Direct Metal Laser Sintering (DMLS) or Selective Laser Melting (SLM). '
                              'This is great for a rather cheap, detailed, and conductive metal prototype or'
                              ' design. ')
                        f.process = 1
                        f.material = 13
                    elif f.metal_concern == 2:  # Strength
                        if f.metal_decision == 1:  # I want the very best for top dollar. ($250+ per print)
                            print('Inconel (SLM) Inconel is a family of superalloys that combine various metals'
                                  ' to form an incredibly durable and strong product. Inconel is used mostly in'
                                  ' aerospace, automotive, or other extreme environments. Inconel is printed mostly'
                                  ' using Selective Laser Melting (SLM). This material is ideal for projects that'
                                  ' must undergo the most inhospitable conditions and continue to perform. ')
                            f.process = 1
                            f.material = 14
                        elif f.metal_decision == 2:  # No, but I still want a high quality metal
                            print('Stainless Steel  (SLM / DMLS) Stainless Steel is an affordable, reliable, '
                                  'and strong alloy type that resists corrosion. An all around reliable material, '
                                  'it is also able to 3D Print in high detail. To top it all off, many services'
                                  ' can coat the Stainless Steel with other metals such as bronze, gold, or '
                                  'silver. Stainless Steel is printed using Direct Metal Laser Sintering (DMLS)'
                                  ' or Selective Laser Melting (SLM). This material is ideal for a cost-effective'
                                  ' and all-around versatile metal project.')
                            f.process = 1
                            f.material = 9
                        else:
                            logger.error('#2')
                    else:
                        logger.error('#1')

                    pass
            elif f.basic_material == 3:  # Other
                if f.other_materials == 1:  # I want my project to be wood-like
                    print('Wood-Like (FDM) There are varying techniques by providers to bring a wood-like print to'
                          ' life, but a common and proven way is a mixture of PLA plastic and wooden fibers.'
                          ' Using this technique, prints can achieve high detail and have a variety of wooden-like'
                          ' finishes. Using this technique, this wood-like material is printed using '
                          'Fused Deposition Modelling (FDM). This material and process is perfect for'
                          ' amazing wood-like trinkets, prototypes, or decor, cheaply and quickly.')
                    f.process = 0
                    f.material = 15
                elif f.other_materials == 2:  # I want my project to be from stone
                    print('Stone (BJ) Stone gives you the power of Michelangelo, easily and for far less cost. '
                          'Stone can be used to make amazing pieces of art that can be full-size if you desire.'
                          ' Finishing options offered by some services polish the printed piece to mimic things '
                          'such as marble in a wide variety of colors. Stone is printed this way using Binder '
                          'Jetting (BJ). This is perfect for ornate and realistic looking statutes, artworks, or'
                          ' trinkets for display. ')
                    f.process = 4
                    f.material = 8
                else:
                    logger.error('#3')
            elif f.basic_material == 0:  # resin
                if f.plastic_concern == 1:  # cost
                    if f.is_food_safe_plastic == 2:  # I want my project to be generally safe around food
                        if f.is_functional_or_basic == 1:  # Yes, ... functional as possible for the cost
                            print('PETG (FDM) PETG is a 3D Printer friendly variation of PET, a commonly'
                                  ' used plastic that is found in anything from clothing fibers to food '
                                  'packaging. It is a somewhat newer 3D Printing material that boasts the'
                                  ' strength of traditional ABS and the simplicity of PLA. It is printed '
                                  'using Fused Deposition Modeling (FDM). In short, its a simple staple '
                                  'for strong, durable, and simple prints. Great for prototypes that need to '
                                  'handle stress.')
                            f.process = 0
                            f.material = 3
                        elif f.is_functional_or_basic == 2:  # No, I just need my ... printed very simply
                            print('PLA (FDM) PLA is a staple material in 3D Printing. It is a very '
                                  'inexpensive and common material that is very commonly used in 3D '
                                  'Printing at home. It has its drawbacks however. PLA tends to very '
                                  'brittle and cannot withstand high temperatures. Most variations are'
                                  ' deemed food-safe and is semi-biodegradable as well. PLA is printed '
                                  'using Fused Deposition Modeling (FDM). Overall, it is perfect for '
                                  'creating cheap first-time prototypes and visual representations of '
                                  'your creations.')
                            f.process = 0
                            f.material = 0
                        else:
                            logger.error('#4')
                    elif f.is_food_safe_plastic == 3:  # No, I don't need my project to be foodsafe
                        if f.plastic_decision == 1:  # Yes, .. to pay slightly more to get a better material
                            print('Nylon (FDM) Nylon is a family of synthetic polymers that are used in '
                                  'countless everyday items. Compared to other basic filament materials '
                                  'for 3D Printing, Nylon is consider a top contender for strength, '
                                  'durability, and even flexibility. This overall performance comes a '
                                  'slightly higher price than other basic filaments, but is often '
                                  'considered worth it. For the most cost effective route, Nylon can '
                                  'be made with Fused Deposition Modeling. Overall, it is a strong and'
                                  ' versatile material that is great for working prototypes and even '
                                  'mechanical parts. ')
                            f.process = 0
                            f.material = 6
                        elif f.plastic_decision == 2:  # No I want my project to pretty simple for a pretty low price
                            print('PETG (FDM) PETG is a 3D Printer friendly variation of PET, a commonly used'
                                  ' plastic that is found in anything from clothing fibers to food packaging. '
                                  'It is a somewhat newer 3D Printing material that boasts the strength of '
                                  'traditional ABS and the simplicity of PLA. It is printed using Fused'
                                  ' Deposition Modeling (FDM). In short, its a simple staple for strong, '
                                  'durable, and simple prints. Great for functional prototypes that need'
                                  ' to handle some stress.')
                            f.process = 0
                            f.material = 3
                        else:
                            logger.error('#5')
                elif f.plastic_concern == 2:  # quality
                    if f.heat_resistance == 1:  # I want my project to be able to withstand heat
                        if f.is_extreme_strength == 2:  # I am willing to spend top dollar ($250+)
                            print('PEEK (Various) PEEK or Polyether Ether Ketone is the 3D Printing variant of'
                                  ' PAEK which was designed to withstand extreme temperatures while providing'
                                  ' incredible strength and durability. Due to this incredible strength and '
                                  'durability it is usually limited to automotive, aerospace, or medical '
                                  'industries because of high price. If youre looking for ultimate material'
                                  ' to keep your project operating under the harshest conditions for a '
                                  'premium cost, look no further.')
                            f.process = 8
                            f.material = 16
                            print('PEI (SLA) PEI or Polyetherimide is an extremely robust thermoplastic '
                                  'that can withstand extreme temperatures and stress. It is a close '
                                  'cousin to PEEK plastic with some difference. It is cheaper than '
                                  'PEEK, but boasts less temperature and stress resistance. '
                                  'A popular brand of this is call ULTEM made by SABIC. If youre '
                                  'looking for one of the toughest out there, but want to spend less '
                                  'than PEEK, PEI is the best option.')
                            f.process = 6
                            f.material = 7
                        elif f.is_extreme_strength == 3:  # No I don't need extreme strength and performance
                            if f.is_better_appearance == 2:  # I want a more functional material for my project
                                print('Reinforced Nylons (FDM) Nylon is a family of synthetic polymers that'
                                      ' are used in countless everyday items. Oftentimes, Nylon is '
                                      'reinforced to add durability or heat resistance. A Common '
                                      'examples is Carbon reinforcement to add strength and heat'
                                      ' resistance. Reinforced Nylons are often made with Fused '
                                      'Deposition Modeling. These nylon-variants are perfect for '
                                      'a cost-effective yet strong and durable functional prototype.')
                                f.process = 0
                                f.material = 7
                            elif f.is_better_appearance == 3:  # I want a better looking appearance for my project
                                print('Alumide (FDM) Alumide is Nylon that is combined with flakes of Aluminum.'
                                      ' Alumide provides the durability and heat resistance of aluminum, '
                                      'and the detail and strength of nylon. Projects made from Alumide can'
                                      ' be colored and then polished for amazingly detailed and smooth '
                                      'creations that are strong and resistant to heat. Alumide projects'
                                      ' are made from Fused Deposition Modelling. This is a perfect material'
                                      ' if youre looking for your project to not only be tough and resistant'
                                      ' to wear, but intricate and polished when finished.')
                                f.process = 0
                                f.material = 18
                            else:
                                logger.error('#6')
                        else:
                            logger.error('#7')
                    elif f.heat_resistance == 2:  # My project requires neither heat resistance or flexibility
                        if f.is_highest_detail == 2:  # Yes, I want the highest detail possible
                            if f.is_full_color == 2:  # Yes, I want rich and full colors for my project
                                print('Resins (PolyJet) Resins that are created via PolyJet printing are '
                                      'rightly superior in terms of detail and resolution.  PolyJet printing '
                                      'can print layers as thin as 16 microns (or 1.6% of a single millimeter.)'
                                      ' Objects printed via PolyJet can also be a wide array of colors '
                                      'including transparent. This incredible accuracy comes at a price, '
                                      'as the resin and printing process are costly compared to regular '
                                      'printing methods. This method is ideal for small and extremely '
                                      'intricate prototype designs. It is not recommended for anything '
                                      'other than small projects.')
                                f.process = 7
                                f.material = 19
                            elif f.is_full_color == 3:  # No I don't need my project to have full colors ...
                                print('Resins (SLA) Resins that are printed via SLA are considered one of '
                                      'the best in terms of resolution and fine details. They are at the '
                                      'intersection of superior quality and fast printing. Resins printed '
                                      'via SLA are not as detailed as PolyJet printing, but this offers '
                                      'advantages as SLA is better for printing larger projects. In addition'
                                      ' using SLA for printing Resins are more expensive than more basic '
                                      'printing methods.This method is best if youre looking for speed and '
                                      'accuracy combined for your project. ')
                                f.process = 6
                                f.material = 19
                            else:
                                logger.error('#8')
                        elif f.is_highest_detail == 3:  # I want detail, but don't need the highest detail possible
                            print('Nylons (SLS) Nylon is a family of synthetic polymers that are used in'
                                  ' countless everyday items. Nylon is considered one of the more versatile '
                                  'materials used in 3D printing today. It has strength, flexibility, and '
                                  'durability, all while being fairly cost effective. While Nylon is able to'
                                  ' printed using Fused Deposition Modelling (FDM), for the best quality '
                                  'output we recommend using Selective Laser Sintering (SLS). The SLS '
                                  'process will often times take longer to print and cost more, but '
                                  'the process is able to handle much more complex printing jobs and '
                                  'the output has a definitive edge over its FDM counterpart. ')
                            f.process = 2
                            f.material = 6
                        else:
                            logger.error('#9')

                    elif f.heat_resistance == 3:  # I want my project to be flexible
                        if f.is_able_to_bend == 2:  # I want my project to handle some bending, ...
                            print('Nylons (SLS) Nylon is a family of synthetic polymers that are used in '
                                  'countless everyday items. Nylon is considered one of the more versatile '
                                  'materials used in 3D printing today. It has strength, flexibility, and '
                                  'durability, all while being fairly cost effective. While Nylon is able'
                                  ' to printed using Fused Deposition Modelling (FDM), for the best quality'
                                  ' output we recommend using Selective Laser Sintering (SLS). The right '
                                  'type of Nylon will be not only be strong but flexible as well. This is '
                                  'an ideal material and process for designing functional and durable '
                                  'prototypes, toys, or components that are not brittle and rigid.')
                            f.process = 2
                            f.material = 6
                        elif f.is_able_to_bend == 3:  # I want my project to feel and act almost like rubber
                            print('TPE (FDM) ThermoPlastic Elastomer or TPE is a class of material that is a '
                                  'polymer blend of usually plastic and rubber. By mixing the two it '
                                  'takes distinct characteristics from both. They are not only durable'
                                  ' but have the flexibility of rubber. Common applications of this material'
                                  ' is covers for smartphones, automotive parts. TPE is printed using '
                                  'Fused Deposition Modeling. This material is great for projects that '
                                  'need to be as flexible as possible.')
                            f.process = 0
                            f.material = 4
                        else:
                            logger.error('#10')
                    else:
                        logger.error('#11')

            f.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dashboard:company')

    def get_object(self, queryset=None):
        return Customer.objects.get(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_button'] = False
        if self.request.user.user_type == 1:
            if self.request.user.customer_set.all():
                if self.request.user.customer_set.first().is_advanced_filled:
                    context['back_button'] = True
        return context


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'customer/customer_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CustomerDetailView, self).get_context_data(**kwargs)
        context['customer_pk'] = self.object
        return context
