from django.conf.urls import include, url

from sessao.views import (EditMateriaOrdemDiaView, ExpedienteView,
                          ExplicacaoDelete, ExplicacaoEdit, ExplicacaoView,
                          ListMateriaOrdemDiaView, MateriaOrdemDiaView,
                          MesaView, OradorExpedienteDelete,
                          OradorExpedienteEdit, OradorExpedienteView,
                          PainelView, PresencaOrdemDiaView, PresencaView,
                          ResumoView, sessao_crud, tipo_expediente_crud,
                          tipo_resultado_votacao_crud, tipo_sessao_crud)

urlpatterns_sessao = sessao_crud.urlpatterns + [
    url(r'^(?P<pk>\d+)/expediente$',
        ExpedienteView.as_view(), name='expediente'),
    url(r'^(?P<pk>\d+)/presenca$',
        PresencaView.as_view(), name='presenca'),
    url(r'^(?P<pk>\d+)/painel$',
        PainelView.as_view(), name='painel'),
    url(r'^(?P<pk>\d+)/presencaordemdia$',
        PresencaOrdemDiaView.as_view(),
        name='presencaordemdia'),
    url(r'^(?P<pk>\d+)/oradorexpediente$',
        OradorExpedienteView.as_view(), name='oradorexpediente'),
    url(r'^(?P<pk>\d+)/oradorexpediente/excluir/(?P<oid>\d+)$',
        OradorExpedienteDelete.as_view(), name='oradorexcluir'),
    url(r'^(?P<pk>\d+)/oradorexpediente/editar/(?P<oid>\d+)$',
        OradorExpedienteEdit.as_view(), name='oradoreditar'),
    url(r'^(?P<pk>\d+)/mesa$', MesaView.as_view(), name='mesa'),
    url(r'^(?P<pk>\d+)/materiaordemdia/list$',
        ListMateriaOrdemDiaView.as_view(), name='materiaordemdia_list'),
    url(r'^(?P<pk>\d+)/materiaordemdia/edit/(?P<mid>\d+)$$',
        EditMateriaOrdemDiaView.as_view(), name='materiaordemdia_edit'),
    url(r'^(?P<pk>\d+)/materiaordemdia/create$',
        MateriaOrdemDiaView.as_view(), name='materiaordemdia_create'),
    url(r'^(?P<pk>\d+)/resumo$',
        ResumoView.as_view(), name='resumo'),
    url(r'^(?P<pk>\d+)/explicacao$',
        ExplicacaoView.as_view(), name='explicacao'),
    url(r'^(?P<pk>\d+)/explicacao/excluir/(?P<oid>\d+)$',
        ExplicacaoDelete.as_view(), name='explicacaoexcluir'),
    url(r'^(?P<pk>\d+)/explicacao/editar/(?P<oid>\d+)$',
        ExplicacaoEdit.as_view(), name='explicacaoeditar'),
]
sessao_urls = urlpatterns_sessao, sessao_crud.namespace, sessao_crud.namespace

urlpatterns = [
    url(r'^sessao/', include(urlpatterns_sessao,
                             sessao_crud.namespace, sessao_crud.namespace)),
    url(r'^sistema/sessao-plenaria/tipo/', include(tipo_sessao_crud.urls)),
    url(r'^sistema/sessao-plenaria/tipo-resultado-votacao/',
        include(tipo_resultado_votacao_crud.urls)),
    url(r'^sistema/sessao-plenaria/tipo-expediente/',
        include(tipo_expediente_crud.urls)),
]
