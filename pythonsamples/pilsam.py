# create login, logout and sign up user buttons
import json
import uuid
from types import SimpleNamespace as Obj

import re
discourse_ctx = Obj()
# stmt = {"children":[{"children":[{"properties":{"JJ":0.6377667784690857,"component_name_pos":0.6377667784690857,"noun_singular":0.6377667784690857,"text":1.0,"V+":1.0,"ui":0.0004966385961755678},"start_pos":7,"end_pos":14,"text":"welcome","score":0.0004966385961755678}],"name":"component_name","digest":{"children":[],"text":"welcome"},"start_pos":7,"end_pos":14,"text":"welcome","score":0.0004966385961755678},{"name":"component_kind","properties":{"ui_component_kind":[["section",1.0]],"NN":0.9994664788246155,"component_name_pos":0.9994664788246155,"noun_singular":0.9994664788246155,"NN+":1.0,"text":1.0},"start_pos":15,"end_pos":22,"text":"section","score":1.0}],"name":"component","start_pos":7,"end_pos":22,"text":"welcome section","score":0.5002483192980878}
# stmt={"children":[{"name":"component_name","properties":{"component":[[[{"kind":"section","id":"p5485d068-8512-11ea-97fb-f82819e7195d","datatype":"text"}],1.0]],"appname_any":1.0,"NNP":0.8016880750656128,"component_name_pos":0.8016880750656128,"noun_singular":0.8016880750656128,"V+":1.0,"text":1.0,"ui":2.9529537993439345e-06},"digest":{"children":[{"name":"name","properties":{"component":[[[{"kind":"section","id":"p5485d068-8512-11ea-97fb-f82819e7195d","datatype":"text"}],1.0]],"appname_any":1.0,"NNP":0.8016880750656128,"component_name_pos":0.8016880750656128,"noun_singular":0.8016880750656128,"V+":1.0,"text":1.0,"ui":2.9529537993439345e-06},"start_pos":6,"end_pos":13,"text":"welcome","score":1.0}],"name":"component_name","start_pos":6,"end_pos":13,"text":"welcome","score":0.5},"start_pos":6,"end_pos":13,"text":"welcome","score":1.0},{"name":"component_kind","properties":{"ui_component_kind":[["section",1.0]],"NN":0.9993385672569275,"component_name_pos":0.9993385672569275,"noun_singular":0.9993385672569275,"NN+":1.0,"text":1.0},"start_pos":14,"end_pos":21,"text":"section","score":1.0}],"name":"component","start_pos":6,"end_pos":21,"text":"welcome section","score":1.0}

stmt = {"children":[{"children":[{"properties":{"NNP":0.8242617249488831,"component_name_pos":0.8242617249488831,"noun_singular":0.8242617249488831,"text":1.0,"NNP+":1.0,"ui":3.6834198875943804e-06},"start_pos":9,"end_pos":18,"text":"dashboard","score":3.6834198875943804e-06}],"name":"component_name","digest":{"children":[{"name":"op","properties":{"op":[["dashboard",1.0]],"NNP":0.8242617249488831,"component_name_pos":0.8242617249488831,"noun_singular":0.8242617249488831,"NNP+":1.0,"text":1.0},"start_pos":9,"end_pos":18,"text":"dashboard","score":1.0}],"name":"component_name","start_pos":9,"end_pos":18,"text":"dashboard","score":0.5},"start_pos":9,"end_pos":18,"text":"dashboard","score":3.6834198875943804e-06},{"name":"component_kind","properties":{"ui_component_kind":[["page",1.0]],"NN":0.9996531009674072,"component_name_pos":0.9996531009674072,"noun_singular":0.9996531009674072,"V+":1.0,"text":1.0},"start_pos":19,"end_pos":23,"text":"page","score":1.0}],"name":"component","start_pos":9,"end_pos":23,"text":"dashboard page","score":0.5000018417099438}

view_kinds = ['section','card']

def create_stmt(domain, action, component_role, component_kind):
    stmt = {
          'domain' : domain
        , 'intent' : { 'action' : action, 'component_role' : component_role}
        , 'component_kind' : component_kind
    }
    return stmt

def add_field(stmt, field_name, **kw_args):
    stmt[field_name] = field = {}
    for key, value in kw_args.items():
        field[key] = value

def add_field_value(stmt, field_name, value):
    stmt[field_name] = value

def find_dict(chunk, key):
    return next((item for item in chunk.get('children') if item.get('name') == key), None)

def get_uuid():
    return f"p{str(uuid.uuid1())}" #appended p for dreamer - Css won't support num as first digits for id

def process_digest(component_name_node):
    entity_name, operation = None, None
    for child in component_name_node.get('digest',[]).get('children',[]):
        if child.get("name") == 'name':
            entity_name = child.get("text")
        if child.get("name") == 'op':
            operation = child.get("properties").get("op")[0][0]
    return entity_name, operation

def get_component_kind(component):
    component_kind = None
    for child in component.get('children',[]):
        try:
            component_kind = child.get('properties').get('ui_component_kind')[0][0]
            break
        except:
            continue

    if component_kind is None:
        component_kind = 'field' #no component kind exists for the item
    return component_kind

def get_current_context_component_id(properties,discourse_ctx,component_kind):
    id = None
    if properties is not None:
        lst_component = None
        try:
            lst_component =  properties.get("component")
        except:
            children = properties.get('children',[])
            if len(children) == 1:
                if children[0].get("component") is not None:
                    lst_component =  children[0].get("component")

        if lst_component is not None:
            for tag in lst_component[0][0]:
                if tag['kind'] == component_kind:
                    id = tag.get('id')
                    break
    return id

def gen_pil_component(component):
    pils = []
    component_name_node = find_dict(component,'component_name')
    component_kind = get_component_kind(component)
    id = get_current_context_component_id(component_name_node.get('properties'), discourse_ctx, component_kind)

    if id is None:
        view_pil = None
        entity_pil = None
        id = get_uuid()
        is_new = True
        part_of = {}#{id: discourse_ctx.current_page.id}
        entity_name, view_operation = process_digest(component_name_node)
        print('process_digest ',entity_name, view_operation)
        if entity_name:
            entity_pil = create_stmt("mvc", action="create", component_role="model", component_kind='entity')
            model_ref = get_uuid()
            add_field(entity_pil, 'name', value=entity_name, ref=model_ref)

        if view_operation:
            view_pil = create_stmt("mvc", action="create", component_role="ui", component_kind='view')
            view_ref = get_uuid()
            add_field_value(view_pil, 'name', { 'value' :  'page_name' , 'ref' : view_ref})
            add_field_value(view_pil, 'component_op', view_operation)
            add_field_value(view_pil, 'has',  {'xref': 'entity_ref', 'component_kind': 'entity'})
            # add_field_value(stmt, 'part_of',  {'xref': page_ref, 'component_kind': 'page'})

        component_subkind = None
        if component_kind in view_kinds:
            component_subkind = component_kind
            component_kind = 'view'

        ui_pil = {
          'domain': 'mvc',
          'intent': {
            'component_role': 'ui'
          },
          'component_kind': component_kind,
          'name': {
            'is_new': is_new,
            'id': id,
            'value': component_name_node.get('text')
          },
          'part_of': part_of
        }
        if component_subkind is not None:
            ui_pil['component_subkind'] = component_subkind
        pils.append(ui_pil)
        if view_pil:
            pils.append(view_pil)
        if entity_pil:
            pils.append(entity_pil)
    return pils

def get_pil_by_component_role(pils, role):
    return next((pil for pil in pils if pil['intent']['component_role'] == role), None)
    # return [pil for pil in pils if ]
print(get_pil_by_component_role(gen_pil_component(stmt),'ui'))
