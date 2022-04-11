#!/usr/bin/env python

# BallnStick creates a ball and stick representation of an object
# Add_VDW creates a copy of an object with full-sized, transparent spheres
# Bondi VDW values added below to override default Pymol settings

from pymol import cmd

# Bondi VDW values
cmd.alter("elem Ac", "vdw=2.00")
cmd.alter("elem Al", "vdw=2.00")
cmd.alter("elem Am", "vdw=2.00")
cmd.alter("elem Sb", "vdw=2.00")
cmd.alter("elem Ar", "vdw=1.88")
cmd.alter("elem As", "vdw=1.85")
cmd.alter("elem At", "vdw=2.00")
cmd.alter("elem Ba", "vdw=2.00")
cmd.alter("elem Bk", "vdw=2.00")
cmd.alter("elem Be", "vdw=2.00")
cmd.alter("elem Bi", "vdw=2.00")
cmd.alter("elem Bh", "vdw=2.00")
cmd.alter("elem B ", "vdw=2.00")
cmd.alter("elem Br", "vdw=1.85")
cmd.alter("elem Cd", "vdw=1.58")
cmd.alter("elem Cs", "vdw=2.00")
cmd.alter("elem Ca", "vdw=2.00")
cmd.alter("elem Cf", "vdw=2.00")
cmd.alter("elem C ", "vdw=1.70")
cmd.alter("elem Ce", "vdw=2.00")
cmd.alter("elem Cl", "vdw=1.75")
cmd.alter("elem Cr", "vdw=2.00")
cmd.alter("elem Co", "vdw=2.00")
cmd.alter("elem Cu", "vdw=1.40")
cmd.alter("elem Cm", "vdw=2.00")
cmd.alter("elem Ds", "vdw=2.00")
cmd.alter("elem Db", "vdw=2.00")
cmd.alter("elem Dy", "vdw=2.00")
cmd.alter("elem Es", "vdw=2.00")
cmd.alter("elem Er", "vdw=2.00")
cmd.alter("elem Eu", "vdw=2.00")
cmd.alter("elem Fm", "vdw=2.00")
cmd.alter("elem F ", "vdw=1.47")
cmd.alter("elem Fr", "vdw=2.00")
cmd.alter("elem Gd", "vdw=2.00")
cmd.alter("elem Ga", "vdw=1.87")
cmd.alter("elem Ge", "vdw=2.00")
cmd.alter("elem Au", "vdw=1.66")
cmd.alter("elem Hf", "vdw=2.00")
cmd.alter("elem Hs", "vdw=2.00")
cmd.alter("elem He", "vdw=1.40")
cmd.alter("elem Ho", "vdw=2.00")
cmd.alter("elem In", "vdw=1.93")
cmd.alter("elem I ", "vdw=1.98")
cmd.alter("elem Ir", "vdw=2.00")
cmd.alter("elem Fe", "vdw=2.00")
cmd.alter("elem Kr", "vdw=2.02")
cmd.alter("elem La", "vdw=2.00")
cmd.alter("elem Lr", "vdw=2.00")
cmd.alter("elem Pb", "vdw=2.02")
cmd.alter("elem Li", "vdw=1.82")
cmd.alter("elem Lu", "vdw=2.00")
cmd.alter("elem Mg", "vdw=1.73")
cmd.alter("elem Mn", "vdw=2.00")
cmd.alter("elem Mt", "vdw=2.00")
cmd.alter("elem Md", "vdw=2.00")
cmd.alter("elem Hg", "vdw=1.55")
cmd.alter("elem Mo", "vdw=2.00")
cmd.alter("elem Nd", "vdw=2.00")
cmd.alter("elem Ne", "vdw=1.54")
cmd.alter("elem Np", "vdw=2.00")
cmd.alter("elem Ni", "vdw=1.63")
cmd.alter("elem Nb", "vdw=2.00")
cmd.alter("elem N ", "vdw=1.55")
cmd.alter("elem No", "vdw=2.00")
cmd.alter("elem Os", "vdw=2.00")
cmd.alter("elem O ", "vdw=1.52")
cmd.alter("elem Pd", "vdw=1.63")
cmd.alter("elem P ", "vdw=1.80")
cmd.alter("elem Pt", "vdw=1.72")
cmd.alter("elem Pu", "vdw=2.00")
cmd.alter("elem Po", "vdw=2.00")
cmd.alter("elem K ", "vdw=2.75")
cmd.alter("elem Pr", "vdw=2.00")
cmd.alter("elem Pm", "vdw=2.00")
cmd.alter("elem Pa", "vdw=2.00")
cmd.alter("elem Ra", "vdw=2.00")
cmd.alter("elem Rn", "vdw=2.00")
cmd.alter("elem Re", "vdw=2.00")
cmd.alter("elem Rh", "vdw=2.00")
cmd.alter("elem Rb", "vdw=2.00")
cmd.alter("elem Ru", "vdw=2.00")
cmd.alter("elem Rf", "vdw=2.00")
cmd.alter("elem Sm", "vdw=2.00")
cmd.alter("elem Sc", "vdw=2.00")
cmd.alter("elem Sg", "vdw=2.00")
cmd.alter("elem Se", "vdw=1.90")
cmd.alter("elem Si", "vdw=2.10")
cmd.alter("elem Ag", "vdw=1.72")
cmd.alter("elem Na", "vdw=2.27")
cmd.alter("elem Sr", "vdw=2.00")
cmd.alter("elem S ", "vdw=1.80")
cmd.alter("elem Ta", "vdw=2.00")
cmd.alter("elem Tc", "vdw=2.00")
cmd.alter("elem Te", "vdw=2.06")
cmd.alter("elem Tb", "vdw=2.00")
cmd.alter("elem Tl", "vdw=1.96")
cmd.alter("elem Th", "vdw=2.00")
cmd.alter("elem Tm", "vdw=2.00")
cmd.alter("elem Sn", "vdw=2.17")
cmd.alter("elem Ti", "vdw=2.00")
cmd.alter("elem W ", "vdw=2.00")
cmd.alter("elem U ", "vdw=1.86")
cmd.alter("elem V ", "vdw=2.00")
cmd.alter("elem Xe", "vdw=2.16")
cmd.alter("elem Yb", "vdw=2.00")
cmd.alter("elem Y ", "vdw=2.00")
cmd.alter("elem Zn", "vdw=1.39")
cmd.alter("elem Zr", "vdw=2.00")
cmd.rebuild()

# workspace settings
cmd.bg_color("white")
cmd.set("ray_opaque_background", "off")
cmd.set("orthoscopic", 0)
cmd.set("transparency", 0.5)
cmd.set("dash_gap", 0)
cmd.set("ray_trace_mode", 1)
cmd.set("ray_texture", 2)
cmd.set("antialias", 3)
cmd.set("ambient", 0.5)
cmd.set("spec_count", 5)
cmd.set("shininess", 50)
cmd.set("specular", 1)
cmd.set("reflect", .1)
cmd.space("cmyk")

@cmd.extend
def BallnStick():
    cmd.color("gray30","elem C")
    cmd.set("dash_gap",0.01)
    cmd.set("dash_radius",0.035)
    cmd.set("surface_quality", 2)
    cmd.set("surface_type", 4)
    #cmd.set("spec_reflect", 0)
    cmd.set("depth_cue", "off")
    preset.ball_and_stick(mode=1)

# From https://github.com/rmera/ncipy/blob/master/nci.py
@cmd.extend
def nci(arg1, arg2, arg3):
    densf=arg1+"-dens"
    gradf=arg1+"-grad"
    cmd.isosurface("grad",gradf, 0.5)
    cmd.ramp_new("ramp", densf, [int(arg2),int(arg3)], "rainbow")
    cmd.set("surface_color", "ramp", "grad")
    cmd.set('two_sided_lighting',value=1)

# defines VDW Sphere settings
@cmd.extend
def spin_density_plot( arg1 , arg2 ):
    cmd.load(arg1+".cube")
    cmd.isosurface("spin_isoA", arg1 , float(arg2))
    cmd.isosurface("spin_isoB", arg1 , -float(arg2))
    cmd.color("red","spin_isoA")
    cmd.color("blue","spin_isoB")
    # cmd.ramp_new("ramp", arg1, color="[red, blue]")
    # cmd.set("surface_color","ramp", "spin_iso")
    #cmd.set("surface_quality",3)
    #cmd.set("ray_texture", 2)
    #cmd.set("antialias", 3)
    #cmd.set("ambient", 0.5)
    #cmd.set("spec_count", 5)
    #cmd.set("shininess", 50)
    #cmd.set("specular", 1)
    cmd.set("transparency",0.7)

@cmd.extend
def mo_plot( arg1, arg2):
    #postive and negative defined as different surfaces for different color
    cmd.isosurface("homo_isoA", arg1 ,float(arg2))
    cmd.isosurface("homo_isoB", arg1 ,-float(arg2))
    cmd.color("red","homo_isoA")
    cmd.color("blue","homo_isoB")
    #cmd.set("surface_quality",3)
    #cmd.set("ray_texture", 2)
    #cmd.set("antialias", 3)
    #cmd.set("ambient", 0.5)
    #cmd.set("spec_count", 5)
    #cmd.set("shininess", 50)
    #cmd.set("specular", 1)
    cmd.set("transparency",0.5)


@cmd.extend
def density_plot( arg1 , arg2 ):
    cmd.load(arg1+".cube")
    cmd.isosurface("dens_surface_"+str(arg2), arg1 , float(arg2))
    cmd.isosurface("dens_surface_-"+str(arg2), arg1 , float(arg2))
    cmd.set("surface_color", "red", "dens_surface_"+str(arg2))
    cmd.set("surface_color", "blue", "dens_surface_-"+str(arg2))
    cmd.rebuild()
    # cmd.set("surface_color","ramp", "spin_iso")
    # cmd.ramp_new("ramp", arg1, color="[red, blue]")
    # cmd.set("surface_color","ramp", "spin_iso")
    #cmd.set("surface_quality",3)
    #cmd.set("ray_texture", 2)
    #cmd.set("antialias", 3)
    #cmd.set("ambient", 0.5)
    #cmd.set("spec_count", 5)
    #cmd.set("shininess", 50)
    #cmd.set("specular", 1)
    cmd.set("transparency",0.7)

@cmd.extend
def esp_plot( arg1 , arg2, arg3):
    #density
    cmd.load(arg1+".cube")
    #esp
    cmd.load(arg2+".cube")
    #ramp
    stored.ramp_vals = [-.1,-.05,.0,.05,.1]
    stored.ramp_cols = ['red', 'yellow', 'green', 'cyan', 'blue']
    cmd.ramp_new("esp_ramp", arg2, stored.ramp_vals, stored.ramp_cols)

    cmd.isosurface("esp_surface_"+str(arg3), arg1 , float(arg3))
    cmd.set("surface_color","esp_ramp", "esp_surface_"+str(arg3))
    # cmd.ramp_new("ramp", arg1, color="[red, blue]")
    # cmd.set("surface_color","ramp", "spin_iso")
    #cmd.set("surface_quality",3)
    #cmd.set("ray_texture", 2)
    #cmd.set("antialias", 3)
    #cmd.set("ambient", 0.5)
    #cmd.set("spec_count", 5)
    #cmd.set("shininess", 50)
    #cmd.set("specular", 1)
    cmd.set("transparency",0.5)
