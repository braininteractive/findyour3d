$(document).ready(function () {
    var saveButton = $('#save');
    var blurb = $('#blurb');
    var tipBody = $('#tipBody');
    var tipTitle = $('#tipTitle');

    var basicMaterial = $('#id_basic_material');
    var preciousMetal = $('#id_is_precious_metal');
    var metalConcern = $('#id_metal_concern');
    var metalDecision = $('#id_metal_decision');
    var otherMaterials = $('#id_other_materials');
    var plasticConcern = $('#id_plastic_concern');
    var foodSafePlastic = $('#id_is_food_safe_plastic');
    var plasticDecision = $('#id_plastic_decision');
    var heatResistance = $('#id_heat_resistance');
    var extremeStrength = $('#id_is_extreme_strength');
    var highestDetail = $('#id_is_highest_detail');
    var functionalOrBasic = $('#id_is_functional_or_basic');
    var ableToBend = $('#id_is_able_to_bend');
    var betterAppearance = $('#id_is_better_appearance');
    var fullColor = $('#id_is_full_color');

    var preciousMetalBlock = $('#div_id_is_precious_metal');
    var metalConcernBlock = $('#div_id_metal_concern');
    var metalDecisionBlock = $('#div_id_metal_decision');
    var otherMaterialsBlock = $('#div_id_other_materials');
    var plasticConcernBlock = $('#div_id_plastic_concern');
    var foodSafePlasticBlock = $('#div_id_is_food_safe_plastic');
    var functionalOrBasicBlock = $('#div_id_is_functional_or_basic');
    var plasticDecisionBlock = $('#div_id_plastic_decision');
    var heatResistanceBlock = $('#div_id_heat_resistance');
    var extremeStrengthBlock = $('#div_id_is_extreme_strength');
    var betterAppearanceBlock = $('#div_id_is_better_appearance');
    var highestDetailBlock = $('#div_id_is_highest_detail');
    var fullColorBlock = $('#div_id_is_full_color');
    var ableToBendBlock = $('#div_id_is_able_to_bend');

    var all = [saveButton, preciousMetalBlock, metalConcernBlock, metalDecisionBlock, otherMaterialsBlock,
        plasticConcernBlock, foodSafePlasticBlock, functionalOrBasicBlock, plasticDecisionBlock,
        heatResistanceBlock, extremeStrengthBlock, betterAppearanceBlock, highestDetailBlock,
        fullColorBlock, ableToBendBlock];

    $.each(all, function(){ $(this).hide()});

    basicMaterial.val(4);  // set init val to null

    basicMaterial.on('change', function () {
        basicMaterial.attr('readonly', true);
        basicMaterial.prop('disabled', true);

        $('#div_id_basic_material').append('<small> <a onclick="location.reload()">Change basic material</a> </small>');
        // metals
        if (this.value==1){
            preciousMetalBlock.show();
            preciousMetal.on('change', function () {
                saveButton.hide();
                blurb.hide();
                if (this.value==3){
                    metalConcernBlock.show();
                    metalConcern.on('change', function () {
                        saveButton.hide();
                        blurb.hide();
                        if (this.value==2){ // strength
                            metalDecisionBlock.show();
                            metalDecision.on('change', function () {
                                if (this.value==1){ // I want the very best for top dollar. ($250+ per print)
                                    saveButton.show();
                                    tipTitle.text("Inconel (SLM)");
                                    tipBody.text("Inconel is a family of superalloys that combine various metals to form an incredibly durable and strong product. Inconel is used mostly in aerospace, automotive, or other extreme environments. Inconel is printed mostly using Selective Laser Melting (SLM). This material is ideal for projects that must undergo the most inhospitable conditions and continue to perform. ");
                                    blurb.show();
                                }
                                if (this.value==2){ // No, but I still want a high quality metal
                                    saveButton.show();
                                    tipTitle.text("Stainless Steel  (SLM / DMLS)");
                                    tipBody.text("Stainless Steel is an affordable, reliable, and strong alloy type that resists corrosion. An all around reliable material, it is also able to 3D Print in high detail. To top it all off, many services can coat the Stainless Steel with other metals such as bronze, gold, or silver. Stainless Steel is printed using Direct Metal Laser Sintering (DMLS) or Selective Laser Melting (SLM). This material is ideal for a cost-effective and all-around versatile metal project.");
                                    blurb.show();
                                }

                                if (this.value==0){
                                    saveButton.hide();
                                    blurb.hide();
                                }
                            })
                        }
                        if (this.value==1){ // Conductivity
                            metalDecisionBlock.hide();
                            metalDecision.val(0);

                            saveButton.show();
                            tipTitle.text("Copper (SLM / DMLS)");
                            tipBody.text("Copper is a commonly used conductive metal that is rather inexpensive even to 3D Print. It offers good resistance to wear and can be polished down to reveal rather ornate features, if required. Copper is printed using Direct Metal Laser Sintering (DMLS) or Selective Laser Melting (SLM). This is great for a rather cheap, detailed, and conductive metal prototype or design. ");
                            blurb.show();
                        }
                        if (this.value==0){
                            metalDecisionBlock.hide();
                            metalDecision.val(0);

                            saveButton.hide();
                            blurb.hide();
                        }
                    })
                }
                if (this.value==2){ // is precious metal
                    saveButton.show();
                    tipTitle.text("Silver / Gold (DMLS / SLM)");
                    tipBody.text("Gold or Silver are obvious choices for things like jewelry or trinkets that are ornate and luxurious. Their beauty and rarity come with at a price, as they are both hard to print and are very expensive. They are printed via Direct Metal Laser Sintering (DMLS) or Selective Laser Melting (SLM). This is ideal for a project that stands above in beauty and is worth every penny.");
                    blurb.show();
                }
            })
        }
        // other
        if (this.value==3){
            otherMaterialsBlock.show();
            otherMaterials.on('change', function () {
                if (this.value==1){ // I want my project to be wood-like
                    saveButton.show();
                    tipTitle.text("Wood-Like (FDM)");
                    tipBody.text("There are varying techniques by providers to bring a wood-like print to life, but a common and proven way is a mixture of PLA plastic and wooden fibers. Using this technique, prints can achieve high detail and have a variety of wooden-like finishes. Using this technique, this wood-like material is printed using Fused Deposition Modelling (FDM). This material and process is perfect for amazing wood-like trinkets, prototypes, or decor, cheaply and quickly.");
                    blurb.show();
                }
                if (this.value==2){ // I want my project to be from stone
                    saveButton.show();
                    tipTitle.text("Stone (BJ)");
                    tipBody.text("Stone gives you the power of Michelangelo, easily and for far less cost. Stone can be used to make amazing pieces of art that can be full-size if you desire. Finishing options offered by some services polish the printed piece to mimic things such as marble in a wide variety of colors. Stone is printed this way using Binder Jetting (BJ). This is perfect for ornate and realistic looking statutes, artworks, or trinkets for display. ");
                    blurb.show();
                }
            })
        }
        // resin
        if (this.value==0){
            plasticConcernBlock.show();
            plasticConcern.on('change', function () {
                saveButton.hide();
                blurb.hide();
                highestDetailBlock.hide();
                highestDetail.val(0);
                ableToBendBlock.hide();
                ableToBend.val(0);
                extremeStrengthBlock.hide();
                extremeStrength.val(0);

                if (this.value==1){ // cost
                    heatResistanceBlock.hide();
                    heatResistance.val(0);

                    foodSafePlasticBlock.show();
                    foodSafePlastic.on('change', function () {
                        saveButton.hide();
                        blurb.hide();
                        if (this.value==2){ // I want my project to be generally safe around food
                            plasticDecisionBlock.hide();
                            plasticDecision.val(0);

                            functionalOrBasicBlock.show();
                            functionalOrBasic.on('change', function () {
                                if (this.value==1){ // Yes, ... functional as possible for the cost
                                    tipTitle.text("PETG (FDM)");
                                    tipBody.text("PETG is a 3D Printer friendly variation of PET, a commonly used plastic that is found in anything from clothing fibers to food packaging. It is a somewhat newer 3D Printing material that boasts the strength of traditional ABS and the simplicity of PLA. It is printed using Fused Deposition Modeling (FDM). In short, it's a simple staple for strong, durable, and simple prints. Great for prototypes that need to handle stress.");
                                    blurb.show();
                                    saveButton.show();
                                }
                                if (this.value==2){ // No, I just need my ... printed very simply
                                    tipTitle.text("PLA (FDM)");
                                    tipBody.text("PLA is a staple material in 3D Printing. It is a very inexpensive and common material that is very commonly used in 3D Printing at home. It has it's drawbacks however. PLA tends to very brittle and cannot withstand high temperatures. Most variations are deemed food-safe and is semi-biodegradable as well. PLA is printed using Fused Deposition Modeling (FDM). Overall, it is perfect for creating cheap first-time prototypes and visual representations of your creations.");
                                    blurb.show();
                                    saveButton.show();
                                }

                                if (this.value==0){
                                    saveButton.hide();
                                    blurb.hide();
                                }
                            })
                        }
                        if (this.value==3){ // No, I don't need my project to be foodsafe
                            functionalOrBasicBlock.hide();
                            functionalOrBasic.val(0);

                            plasticDecisionBlock.show();
                            plasticDecision.on('change', function () {
                                if (this.value==1){ // Yes, .. to pay slightly more to get a better material
                                    tipTitle.text("Nylon (FDM) ");
                                    tipBody.text("Nylon is a family of synthetic polymers that are used in countless everyday items. Compared to other basic filament materials for 3D Printing, Nylon is consider a top contender for strength, durability, and even flexibility. This overall performance comes a slightly higher price than other basic filaments, but is often considered worth it. For the most cost effective route, Nylon can be made with Fused Deposition Modeling. Overall, it is a strong and versatile material that is great for working prototypes and even mechanical parts. ");
                                    blurb.show();
                                    saveButton.show();
                                }
                                if (this.value==2){ // No I want my project to pretty simple for a pretty low price
                                    tipTitle.text("PETG (FDM)");
                                    tipBody.text("PETG is a 3D Printer friendly variation of PET, a commonly used plastic that is found in anything from clothing fibers to food packaging. It is a somewhat newer 3D Printing material that boasts the strength of traditional ABS and the simplicity of PLA. It is printed using Fused Deposition Modeling (FDM). In short, it's a simple staple for strong, durable, and simple prints. Great for functional prototypes that need to handle some stress.");
                                    blurb.show();
                                    saveButton.show();
                                }

                                if (this.value==0){
                                    saveButton.hide();
                                    blurb.hide();
                                }

                            })
                        }
                        if (this.value==1){
                            plasticDecisionBlock.hide();
                            plasticDecision.val(0);
                            functionalOrBasicBlock.hide();
                            functionalOrBasic.val(0);
                        }
                    })
                }
                if (this.value==2){ // quality
                    foodSafePlasticBlock.hide();
                    foodSafePlastic.val(0);
                    functionalOrBasicBlock.hide();
                    functionalOrBasic.val(0);
                    plasticDecisionBlock.hide();
                    plasticDecision.val(0);

                    heatResistanceBlock.show();
                    heatResistance.on('change', function () {
                        saveButton.hide();
                        blurb.hide();
                        betterAppearanceBlock.hide();
                        betterAppearance.val(0);
                        ableToBendBlock.hide();
                        ableToBend.val(0);

                        if (this.value==1){ // I want my project to be able to withstand heat
                            highestDetailBlock.hide();
                            highestDetail.val(0);
                            ableToBendBlock.hide();
                            ableToBend.val(0);

                            extremeStrengthBlock.show();
                            extremeStrength.on('change', function () {
                                saveButton.hide();
                                blurb.hide();
                                if (this.value==3){ // No I don't need extreme strength and performance
                                    betterAppearanceBlock.show();
                                    betterAppearance.on('change', function () {
                                        if (this.value==2){ // I want a more functional material for my project
                                            saveButton.show();
                                            tipTitle.text("Reinforced Nylons (FDM)");
                                            tipBody.text("Nylon is a family of synthetic polymers that are used in countless everyday items. Oftentimes, Nylon is reinforced to add durability or heat resistance. A Common examples is Carbon reinforcement to add strength and heat resistance. Reinforced Nylons are often made with Fused Deposition Modeling. These nylon-variants are perfect for a cost-effective yet strong and durable functional prototype.");
                                            blurb.show();
                                        }
                                        if (this.value==3){ // I want a better looking appearance for my project
                                            saveButton.show();
                                            tipTitle.text("Alumide (FDM)");
                                            tipBody.text("Alumide is Nylon that is combined with flakes of Aluminum. Alumide provides the durability and heat resistance of aluminum, and the detail and strength of nylon. Projects made from Alumide can be colored and then polished for amazingly detailed and smooth creations that are strong and resistant to heat. Alumide projects are made from Fused Deposition Modelling. This is a perfect material if you're looking for your project to not only be tough and resistant to wear, but intricate and polished when finished.");
                                            blurb.show();
                                        }
                                        if (this.value==1){
                                            saveButton.hide();
                                            blurb.hide();
                                        }
                                    })
                                }
                                if (this.value==2){ // I am willing to spend top dollar ($250+)
                                    betterAppearanceBlock.hide();
                                    betterAppearance.val(0);
                                    saveButton.show();
                                    tipTitle.text("PEEK (Various) PEI (SLA)");
                                    tipBody.text("PEEK or Polyether Ether Ketone is the 3D Printing variant of PAEK which was designed to withstand extreme temperatures while providing incredible strength and durability. Due to this incredible strength and durability it is usually limited to automotive, aerospace, or medical industries because of high price. If you're looking for ultimate material to keep your project operating under the harshest conditions for a premium cost, look no further. PEI or Polyetherimide is an extremely robust thermoplastic that can withstand extreme temperatures and stress. It is a close cousin to PEEK plastic with some difference. It is cheaper than PEEK, but boasts less temperature and stress resistance. A popular brand of this is call ULTEM made by SABIC. If you're looking for one of the toughest out there, but want to spend less than PEEK, PEI is the best option.");
                                    blurb.show();
                                }
                            })
                        }
                        if (this.value==2){ // My project requires neither heat resistance or flexibility
                            extremeStrengthBlock.hide();
                            extremeStrength.val(0);
                            ableToBend.val(0);

                            highestDetailBlock.show();
                            highestDetail.on('change', function () {
                                fullColorBlock.hide();
                                fullColor.val(0);
                                saveButton.hide();
                                blurb.hide();

                                if (this.value==2){ // Yes, I want the highest detail possible
                                    fullColorBlock.show();
                                    fullColor.on('change', function () {
                                        if (this.value==2){ // Yes, I want rich and full colors for my project
                                            saveButton.show();
                                            tipTitle.text("Resins (PolyJet)");
                                            tipBody.text("Resins that are created via PolyJet printing are rightly superior in terms of detail and resolution.  PolyJet printing can print layers as thin as 16 microns (or 1.6% of a single millimeter.) Objects printed via PolyJet can also be a wide array of colors including transparent. This incredible accuracy comes at a price, as the resin and printing process are costly compared to regular printing methods. This method is ideal for small and extremely intricate prototype designs. It is not recommended for anything other than small projects.");
                                            blurb.show();
                                        }
                                        if (this.value==3){ // No I don't need my project to have full colors ...
                                            saveButton.show();
                                            tipTitle.text("Resins (SLA)");
                                            tipBody.text("Resins that are printed via SLA are considered one of the best in terms of resolution and fine details. They are at the intersection of superior quality and fast printing. Resins printed via SLA are not as detailed as PolyJet printing, but this offers advantages as SLA is better for printing larger projects. In addition using SLA for printing Resins are more expensive than more basic printing methods.This method is best if you're looking for speed and accuracy combined for your project. ");
                                            blurb.show();
                                        }

                                        if (this.value==1){
                                            saveButton.hide();
                                            blurb.hide();
                                        }
                                    })
                                }
                                if (this.value==3){ // I want detail, but don't need the highest detail possible
                                    saveButton.show();
                                    tipTitle.text("Nylons (SLS)");
                                    tipBody.text("Nylon is a family of synthetic polymers that are used in countless everyday items. Nylon is considered one of the more versatile materials used in 3D printing today. It has strength, flexibility, and durability, all while being fairly cost effective. While Nylon is able to printed using Fused Deposition Modelling (FDM), for the best quality output we recommend using Selective Laser Sintering (SLS). The SLS process will often times take longer to print and cost more, but the process is able to handle much more complex printing jobs and the output has a definitive edge over it's FDM counterpart. ");
                                    blurb.show();
                                }
                            })
                        }
                        if (this.value==3){ // I want my project to be flexible
                            highestDetailBlock.hide();
                            highestDetail.val(0);
                            extremeStrengthBlock.hide();
                            extremeStrength.val(0);

                            ableToBendBlock.show();
                            ableToBend.on('change', function () {
                                if (this.value==2){ // I want my project to handle some bending, ...
                                    saveButton.show();
                                    tipTitle.text("Nylons (SLS)");
                                    tipBody.text("Nylon is a family of synthetic polymers that are used in countless everyday items. Nylon is considered one of the more versatile materials used in 3D printing today. It has strength, flexibility, and durability, all while being fairly cost effective. While Nylon is able to printed using Fused Deposition Modelling (FDM), for the best quality output we recommend using Selective Laser Sintering (SLS). The right type of Nylon will be not only be strong but flexible as well. This is an ideal material and process for designing functional and durable prototypes, toys, or components that are not brittle and rigid.");
                                    blurb.show();
                                }
                                if (this.value==3){ // I want my project to feel and act almost like rubber
                                    saveButton.show();
                                    tipTitle.text("TPE (FDM)");
                                    tipBody.text("ThermoPlastic Elastomer or TPE is a class of material that is a polymer blend of usually plastic and rubber. By mixing the two it takes distinct characteristics from both. They are not only durable but have the flexibility of rubber. Common applications of this material is covers for smartphones, automotive parts. TPE is printed using Fused Deposition Modeling. This material is great for projects that need to be as flexible as possible.");
                                    blurb.show();
                                }

                                if (this.value==1){
                                    saveButton.hide();
                                    blurb.hide();
                                }
                            })
                        }
                        if (this.value==0){
                            console.log('close heat');
                            highestDetailBlock.hide();
                            highestDetail.val(0);
                            ableToBendBlock.hide();
                            ableToBend.val(0);
                            extremeStrengthBlock.hide();
                            extremeStrength.val(0);
                            fullColorBlock.hide();
                            fullColor.val(0);
                            plasticDecisionBlock.hide();
                            plasticDecision.val(0);
                        }
                    })
                }
                if (this.value==0){
                    console.log('close child');
                    heatResistanceBlock.hide();
                    heatResistance.val(0);
                    highestDetailBlock.hide();
                    highestDetail.val(0);
                    ableToBendBlock.hide();
                    ableToBend.val(0);
                    extremeStrengthBlock.hide();
                    extremeStrength.val(0);
                    fullColorBlock.hide();
                    fullColor.val(0);
                    plasticDecisionBlock.hide();
                    plasticDecision.val(0);
                    foodSafePlasticBlock.hide();
                    foodSafePlastic.val(0);
                    functionalOrBasicBlock.hide();
                    functionalOrBasic.val(0);
                }
            })
        }
    });
    $('form').submit(function(e) {
        $(':disabled').each(function(e) {
            $(this).removeAttr('disabled');
        })
    });

});
