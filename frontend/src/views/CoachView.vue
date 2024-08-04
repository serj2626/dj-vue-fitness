<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import { useToast } from "vue-toastification";
import { useRoute, useRouter } from "vue-router";
const route = useRoute();

const { id } = route.params;
const toast = useToast();
const coach = ref([]);
const showReviews = ref(false);

const getCoach = async () => {
  try {
    const { data } = await axios.get(`/api/workout/trainers/${id}`);
    console.log(data);
    coach.value = data;
  } catch {
    toast.error("Произошла ошибка при получении тренера");
  }
};

onMounted(getCoach);
</script>

<template>
  <div
    class="container mt-[220px] flex gap-4 p-9 rounded-xl shadow-2xl shadow-white"
  >
    <div
      class="w-1/3 mx-auto rounded-2xl flex flex-col items-center justify-center gap-4"
    >
      <img class="" :src="coach.avatar" alt="" />
    </div>

    <div class="w-2/3 text-white">
      <ul>
        <li>{{ coach.first_name }} {{ coach.last_name }}</li>
        <li>{{ coach.position }}</li>
        <li>{{ coach.email }}</li>
        <li>{{ coach.phone }}</li>
        <li>{{ coach.bio }}</li>
        <li @click="showReviews = !showReviews">
          <button >
            Отзывы
          </button>
        </li>
      </ul>
    </div>
  </div>
  <transition name="fade">
    <div v-if="showReviews" class="reviews">
      <h1 class="text-3xl text-center text-white font-extrabold">Отзывы</h1>
      <ul>
        <li>Отзыв</li>
        <li>Отзыв</li>
        <li>Отзыв</li>
        <li>Отзыв</li>
        <li>Отзыв</li>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Nihil corrupti,
        numquam molestias fuga est libero natus deleniti quidem ex saepe animi
        nam tempora voluptatibus voluptate, nesciunt, eos totam quos quia facere
        temporibus tempore adipisci! Officiis beatae fugit veritatis sint ab
        voluptatum consequuntur quisquam repellendus eum in? Numquam, facere.
        Impedit repellendus tenetur exercitationem voluptatum praesentium.
        Repudiandae perspiciatis tenetur reprehenderit corrupti excepturi quod
        repellendus officia expedita ad numquam nostrum repellat molestias error
        mollitia doloribus culpa, a veniam blanditiis natus illo soluta, eos
        necessitatibus atque! Vitae perspiciatis, magnam odio quae voluptatem
        sed nam earum accusantium recusandae totam perferendis ratione voluptas
        fugit, dolorum corrupti ipsam modi ea cum in aperiam, dolorem dicta!
        Sunt recusandae, corrupti illo excepturi qui, architecto repudiandae
        temporibus nulla rem laborum natus amet sapiente provident ipsum beatae
        pariatur deleniti. Repudiandae magni ullam velit mollitia maiores
        ducimus ea sequi? Culpa vel voluptate adipisci commodi explicabo
        voluptatum enim. Soluta maiores necessitatibus animi fuga a ipsam nobis
        quos laborum exercitationem eveniet, tempora architecto cumque, nesciunt
        vero quae velit dolorem? Eaque cupiditate quisquam quo fuga ipsam natus
        doloremque quis, harum rerum repellendus atque similique eveniet officia
        facilis blanditiis consequatur ea veritatis obcaecati nesciunt non cum.
        Consequatur omnis error ab numquam odit! Natus tempora incidunt hic
        vitae omnis similique, quibusdam doloribus, assumenda delectus fuga sunt
        dolorum et ipsam in ab voluptatem voluptate saepe fugiat distinctio
        officia magnam! Illum sequi odio ipsam ea cumque consectetur voluptate
        numquam saepe at, suscipit, reprehenderit non corrupti repellendus
        velit, facilis quo. A vitae voluptate, sit voluptatibus sunt ut dolor
        optio, aliquam dolorem sapiente fugiat deserunt eaque, similique qui?
        Neque cum ipsam iusto, dolor maiores veritatis molestias aspernatur
        voluptate corrupti, debitis corporis tempora, dolore asperiores cumque
        suscipit repellendus deleniti nisi vel pariatur temporibus placeat hic
        minus minima eveniet. Labore perspiciatis blanditiis dolore doloremque
        saepe aperiam repellat reiciendis, aliquam porro id possimus autem
        quidem voluptatum exercitationem aut maxime neque quam magni minima?
        Accusantium nesciunt qui cupiditate veniam debitis voluptates,
        voluptatem velit quia animi, fuga ipsum aliquam quo tenetur, quos porro
        magnam dolore suscipit optio eaque perferendis. Aut fuga nobis
        distinctio, error a officiis accusamus provident voluptatibus nulla
        minus similique, velit nemo molestias debitis odio modi, quas porro
        magnam rerum et quasi veritatis suscipit sint! Ad quo a voluptatem
        doloremque, rerum ullam quasi provident nisi. Vero totam, fugiat maxime
        vel voluptatem quas voluptas saepe atque alias eveniet obcaecati
        corrupti tenetur dolor ipsum excepturi, consequuntur numquam soluta est
        neque earum quos. Tempore dolore delectus officia nisi sed eligendi
        beatae maxime quis dolorum nemo, laboriosam ratione. Laborum tempora
        corrupti nemo? Laudantium dolorum reprehenderit eaque? Quaerat earum
        nihil, perspiciatis est libero odit ut expedita eligendi, ipsam
        provident obcaecati fugit possimus hic distinctio ullam. Vitae, veniam
        aliquid labore corporis magnam, repellat non maxime omnis totam minus
        nemo obcaecati? Doloremque, similique! Voluptas obcaecati impedit
        perferendis alias tempora explicabo unde exercitationem, similique,
        eligendi quis officia, commodi incidunt quidem praesentium error! Quod
        quos quis amet esse laborum, cum quisquam porro, reiciendis sunt
        veritatis, libero quaerat nobis fugiat optio quae sed rerum qui in
        cumque voluptatum aut! Fugit velit illo, praesentium consequatur magni
        ipsam itaque veniam molestiae autem. Voluptatum provident suscipit
        repudiandae eos ipsa ipsum porro sunt, laboriosam esse modi, sint
        reiciendis, sapiente quasi! Tenetur voluptatem rem minima natus. Id at
        voluptatibus laboriosam provident ipsa repellendus quod impedit! Eos
        voluptatum nulla labore cupiditate reiciendis ex accusantium, fugiat ea
        corporis est quo deleniti ipsa hic sed ipsum asperiores id iusto enim
        excepturi eligendi quidem. At nulla saepe illum iste veniam, debitis
        doloribus perspiciatis minima ipsa suscipit ducimus ipsum fugit vitae
        assumenda illo iusto aut, magni exercitationem, corporis dolorem cum
        asperiores? Iure nulla magnam corrupti nesciunt quo labore. Suscipit ea
        at placeat cupiditate quasi, harum eius deserunt facere accusamus illo
        tenetur, laboriosam ipsum velit esse, explicabo adipisci! Voluptatem
        quam ratione nam dolorum vitae, natus esse alias dicta optio laborum
        beatae praesentium repellendus corrupti ad, ea odio, voluptate illum
        nulla obcaecati minus mollitia quaerat qui voluptatum! Veritatis vitae
        cupiditate qui doloremque, quas consectetur, repellat optio quod, earum
        itaque beatae deleniti! Officiis animi cupiditate ratione rerum tempore,
        sed magnam! Dolorum at, et, iusto vel eligendi in aspernatur expedita
        dolore cupiditate harum excepturi accusamus! Dolore delectus, at
        voluptatem reprehenderit quae maxime, omnis totam, assumenda repellendus
        modi cum incidunt harum dolorum earum porro vel odit esse adipisci nihil
        doloribus? Nisi velit eius asperiores magnam consequuntur dignissimos,
        eveniet nam cupiditate corrupti, et consectetur vel ipsum voluptates
        facere perspiciatis aut pariatur natus, commodi iusto nobis autem libero
        soluta quod! Vero voluptatibus illo eos soluta optio, quo quis itaque
        voluptatum iste at modi error exercitationem, in quisquam. Asperiores
        dolores enim rerum esse quisquam vitae corporis fuga nemo ullam maxime?
        Odit quisquam alias delectus architecto molestiae quam aperiam deserunt
        minus! Alias suscipit, vitae consectetur quisquam asperiores ea
        distinctio inventore placeat velit modi dolore similique repudiandae
        iure tempore magnam quo quidem consequatur sequi totam labore animi
        temporibus. Reprehenderit fuga temporibus dolorem ut voluptatibus natus
        repellat aliquam architecto perspiciatis, illum iure beatae alias sequi
        cupiditate labore doloremque odio ipsam ducimus corrupti placeat facere
        nobis quia ipsum. Voluptate aliquid veritatis porro, et nostrum
        voluptatem quod. Officia, atque animi, nulla quod quo non asperiores
        nostrum, voluptatum mollitia vero ipsam adipisci totam quis iusto? Eum
        mollitia ipsum ullam at voluptatibus soluta dolore inventore molestias
        quia ipsam deleniti culpa doloribus eaque dignissimos, quae qui dolorem,
        facilis quisquam sit numquam veritatis id magni quasi? Deserunt
        doloremque accusantium esse dolorem, nihil accusamus atque quam
        perspiciatis aut non voluptas, optio harum dolor tenetur eos facere
        autem culpa beatae et saepe praesentium quidem ipsum unde! Illo fugiat
        minima quaerat recusandae vitae praesentium, necessitatibus deleniti
        aliquid reprehenderit! Voluptate odit porro possimus ex maxime?
        Perferendis quia sapiente molestiae aspernatur omnis, dolor repudiandae
        asperiores sit accusantium sunt, ab eos a rem. Deleniti quae molestias
        distinctio, excepturi fugit est suscipit, consequuntur, dignissimos
        sapiente consequatur magnam nostrum incidunt earum at. Earum molestiae
        amet eos similique, possimus eum explicabo commodi quidem excepturi
        alias cupiditate quae veritatis nulla. Quas laboriosam qui molestias cum
        assumenda natus repellendus sed, maiores at modi dolorem eos ipsam
        voluptatum quisquam unde deleniti iure, quis excepturi inventore
        eligendi numquam saepe. Unde sed mollitia sequi! Obcaecati quaerat
        dignissimos excepturi dolor, fugiat deleniti vitae eveniet. Doloremque
        non dolorum in perspiciatis delectus deleniti distinctio maxime vitae
        tempora molestiae necessitatibus facere earum autem, sequi libero optio!
        Iusto, quidem impedit itaque temporibus hic minus. Sed illo expedita
        cupiditate, ducimus, inventore cumque nesciunt voluptas, aliquam
        suscipit saepe itaque quisquam labore ad qui. Nobis molestias at animi
        officia voluptate quaerat sit quisquam debitis. Deserunt omnis alias
        obcaecati sit illum doloremque facere possimus officia culpa recusandae
        nemo repudiandae voluptates, ipsum hic nihil, ratione explicabo dolores
        neque sint ea asperiores? Doloremque dolor corrupti voluptatibus
        pariatur iste at, culpa sed, unde modi voluptatem saepe iusto, ut error
        eum molestias! Officia sit facilis laborum fuga ex deserunt quaerat.
        Eius optio numquam eligendi provident. Rem repellat nisi, distinctio
        beatae minima quis praesentium nemo dolores reprehenderit quasi unde
        eius reiciendis quibusdam impedit. Atque, fuga suscipit? Similique nulla
        officia soluta quisquam, natus vitae? Magni sit, beatae earum atque sint
        numquam repellat, libero aspernatur sunt maiores dolorem. Molestiae,
        mollitia? Accusamus deserunt asperiores, cum deleniti et numquam
        veritatis quidem aut amet repellat cumque tempora nostrum harum quis
        odio hic ut non quae ipsum? Rerum aliquam numquam tenetur adipisci quos
        dolor deserunt, dicta sint id eligendi tempore natus obcaecati labore
        ratione dolorem sequi, placeat doloremque facere ipsum vitae quae, nihil
        in. Fugit quam eos tenetur, vel at nisi quisquam facere! Veritatis,
        minima, consequatur magnam aut alias dicta nulla itaque esse quia at
        earum sit laborum, explicabo inventore exercitationem praesentium cum
        rerum voluptates impedit! Est quas eaque animi impedit sit, porro itaque
        deserunt quisquam, error soluta ipsum repellendus ullam eum quos
        repellat sunt molestias labore recusandae assumenda cum. Nulla quo
        reprehenderit inventore numquam molestiae quibusdam illo aut corporis
        sit dicta, dignissimos expedita qui blanditiis nemo facere. Facilis
        aliquam vel laboriosam fugit commodi esse rem cum. Nisi excepturi magnam
        exercitationem quibusdam, vitae velit atque rerum laboriosam unde
        assumenda obcaecati dolor cum, quos animi, voluptatum iusto. Eius, est.
        Quas, beatae rem. Impedit cum veniam eius quia soluta vero aperiam sunt
        alias aliquam porro ipsa incidunt repudiandae ipsam fugit, nisi nobis
        magnam magni? Ab optio ducimus dolorum ullam veniam nisi cum impedit!
        Laudantium ex eos ipsam omnis, exercitationem aliquid quasi et quia
        repellendus aperiam! Enim rerum saepe officiis, debitis eaque natus
        architecto commodi esse, veritatis molestiae assumenda facere, tempora
        culpa laudantium sunt adipisci eveniet praesentium. Dolorum quaerat
        deserunt ad reprehenderit rerum unde? Cumque, tempore ut. Porro aperiam
        sequi quos, autem officiis at? Totam dolore incidunt unde repudiandae
        rerum quisquam debitis itaque aliquam culpa quam iure ratione molestias
        animi, deleniti laudantium, ad nam beatae blanditiis. Quam magni
        praesentium repudiandae veritatis, amet officiis doloribus eaque
        exercitationem corporis voluptates repellat harum id laudantium labore
        deleniti dolores voluptatem porro aut. Maxime iure suscipit facere
        recusandae impedit eius accusantium inventore, blanditiis neque nostrum
        in voluptate quasi ad, fuga at quibusdam cum illo eaque pariatur
        adipisci tenetur sit voluptatibus. Ipsum aliquam alias expedita a,
        quibusdam libero minus tempora voluptate qui esse. Tempora recusandae
        cum in eaque debitis blanditiis molestias fugit iusto? Velit inventore
        quos amet iusto, tempore iure harum accusamus nisi assumenda obcaecati
        nihil fugit asperiores maiores atque reprehenderit ducimus dolorum
        voluptates incidunt saepe. Similique cum blanditiis dignissimos! Ad,
        ducimus. Corporis facilis itaque tenetur earum, temporibus blanditiis
        aut doloribus nam possimus odit neque at quaerat, deleniti tempora quod
        tempore aliquam minima enim voluptate beatae. Molestiae, beatae at
        dolore quos libero, magni itaque eius ipsam assumenda, quas ipsum id
        error commodi consectetur totam exercitationem asperiores fugit
        excepturi. Ad alias quis unde officiis incidunt. Qui nemo culpa
        veritatis ut doloremque voluptatum, praesentium nesciunt ex aspernatur.
        Exercitationem nulla libero sint, reprehenderit modi sequi deleniti nemo
        consequuntur, non in numquam ipsum odio molestias soluta cum labore?
        Cumque debitis voluptatem animi? Maxime, illo in blanditiis officiis
        alias possimus recusandae tempora ipsam numquam ullam est fugiat
        mollitia, enim similique tenetur quo nesciunt et assumenda omnis
        eligendi voluptatibus reiciendis minima explicabo laboriosam!
        Praesentium id ad nam facilis. Consequuntur ad sed dignissimos
        reprehenderit in dolorum impedit quibusdam iusto nemo magni nihil, illum
        alias non natus quas, expedita ea cumque debitis labore, dolor dicta
        perspiciatis. Ut nihil ad facilis magnam nesciunt reprehenderit,
        accusantium tempore aliquam a dolor possimus quis qui itaque iste
        tempora eveniet laboriosam voluptates ratione deleniti mollitia quam!
        Tenetur et vel deleniti tempora, laudantium dignissimos est ipsam quod
        unde nesciunt, eos facere incidunt corrupti numquam molestias porro!
        Dicta, non debitis. Perferendis vel natus quia! Aliquid, commodi! Dicta
        laboriosam praesentium a omnis, placeat esse exercitationem possimus
        ipsum natus expedita iure perferendis tenetur ullam sequi enim
        consectetur labore assumenda temporibus animi ratione alias perspiciatis
        distinctio quibusdam mollitia! Esse iusto, necessitatibus quisquam
        tempora, vitae beatae iure repellat accusamus rem maiores id maxime
        perspiciatis atque modi. Quaerat, facere, impedit laudantium vitae ipsa
        quis doloremque veniam veritatis labore fugiat doloribus perspiciatis
        omnis quae, at aperiam odio! Debitis natus atque sequi et numquam
        doloribus omnis quae illum provident ab perferendis eligendi obcaecati,
        iste hic. Eos non autem blanditiis odit asperiores distinctio veniam!
        Voluptas, assumenda consectetur! Nostrum ea possimus, dolore dicta quas
        asperiores in quod fugiat consequuntur repellendus sit optio laudantium
        provident nemo, reprehenderit quasi ducimus, maxime magni et illum
        assumenda eos eaque? Corrupti, ipsam saepe possimus necessitatibus iure
        minus expedita sunt, labore sint soluta quod dignissimos aut architecto
        delectus exercitationem inventore velit quis pariatur id enim deleniti
        eius ipsum. Nam dolorem, praesentium error nesciunt reiciendis
        recusandae tempora laudantium ad, excepturi incidunt fugit autem
        quibusdam minima temporibus quisquam qui animi, officia iusto quaerat
        dolorum. Aliquid iusto tempora cumque exercitationem explicabo sed
        accusantium suscipit distinctio animi autem dolore quia, quaerat
        laboriosam rem quod deleniti. Vel eligendi sunt facere nostrum
        distinctio eaque. Qui beatae officiis tempora ab quos at quam facere
        consequuntur, ipsa ut voluptatibus praesentium eveniet mollitia modi
        vitae amet deserunt voluptates! Suscipit, temporibus ipsum dolorum
        voluptatibus repellat fuga illo ut minima ipsa neque praesentium quod
        adipisci totam, necessitatibus perferendis libero numquam magnam atque
        harum culpa ad! Fugit, itaque deleniti, cum officia sit eveniet error
        eius dolor sint facilis dolore dicta natus ducimus adipisci perspiciatis
        cumque eos assumenda numquam! Harum explicabo iusto quas consectetur
        itaque temporibus tempore inventore unde, ipsum nesciunt corrupti iste
        repudiandae, doloribus, sit architecto! Nobis neque repellendus atque
        necessitatibus amet doloremque rerum aut quibusdam suscipit sequi animi,
        aspernatur mollitia et iusto dolores veritatis quas eligendi alias ipsum
        quis eius error incidunt? Consequatur accusantium praesentium mollitia,
        architecto sapiente quidem molestiae error cupiditate culpa laboriosam
        nemo? Eos, quaerat quam soluta dignissimos illo architecto! Dicta vitae
        sit et hic pariatur unde quidem libero iure consequatur recusandae
        excepturi fugiat explicabo praesentium magnam esse, accusamus est
        mollitia totam quia, corporis cum, porro ab maiores laborum. Quae
        fugiat, perferendis tempore dolores in possimus veniam ipsum dolor
        expedita saepe doloremque illo! Voluptatum laboriosam minus sed
        perferendis animi odio eius vero, autem dignissimos, iure excepturi, ex
        nemo consequatur officia minima et eveniet? Iure natus adipisci,
        expedita dolor asperiores voluptatem architecto ad autem aspernatur
        vero? Alias blanditiis, placeat dolor amet nostrum eaque tempora minima
        corrupti odio molestias laboriosam quia est eius cupiditate vitae, quas
        voluptates at commodi illum accusamus culpa voluptatibus qui! Debitis
        tenetur tempore laudantium sit dicta quia, doloremque, neque repellat
        labore, voluptate ad similique quod ullam repellendus corrupti non
        perferendis natus repudiandae tempora cupiditate eligendi deserunt unde?
        Explicabo exercitationem, consectetur molestias porro illum asperiores
        soluta tempora deserunt enim quas et veritatis laboriosam odit
        accusantium. Commodi, necessitatibus. Dolorum, consequatur eaque quos
        saepe deleniti, iusto aperiam unde dignissimos ex nostrum atque
        repudiandae earum aspernatur quisquam voluptatum nihil sed in eum
        fugiat, harum hic accusantium? Neque tempora aut accusamus animi id rem
        rerum, corporis inventore est nisi harum fugit sint iusto! Cupiditate
        pariatur, nihil reiciendis repudiandae accusantium praesentium. Sit
        laboriosam labore sunt necessitatibus impedit illum, doloremque facilis
        voluptas, magnam amet odit dolorem quibusdam quos quaerat quas qui
        accusantium, possimus est dolores vel atque quae? Officiis odit
        distinctio quod facilis labore sed ex numquam nostrum dolores alias
        dolorum fugiat, consectetur, quibusdam fuga ut eaque voluptates. Modi
        dolore quisquam quia totam quos doloremque iste eveniet, nostrum
        perspiciatis beatae fugiat corporis, voluptates, fuga quae nemo
        exercitationem velit in impedit cumque. Ut molestiae recusandae soluta
        obcaecati dolorum natus suscipit, ratione illum fugiat possimus animi
        hic laborum culpa tempore aliquid tenetur quae vel consequatur
        asperiores totam voluptate minima officiis at! Suscipit voluptates
        similique, neque iste minima minus obcaecati possimus placeat labore
        laudantium, atque ea in necessitatibus velit molestiae, quas fugit ullam
        adipisci ab saepe eius molestias commodi perspiciatis. Enim, voluptate?
        Aliquam perferendis incidunt ratione, ullam eius sequi odio labore
        dignissimos eos provident? Tempore voluptatum consequuntur dignissimos
        optio velit vitae eaque commodi mollitia debitis modi dolorem corrupti,
        laboriosam cum! Quae nostrum optio aut fugiat ipsam molestias
        consectetur a in natus magnam veniam voluptates, fugit illum nesciunt
        provident alias iste id dolorem unde. Eveniet soluta pariatur fugiat
        dignissimos quasi ab voluptate amet nulla quod, sit, saepe fuga
        molestias natus nihil ad itaque excepturi officiis commodi impedit
        labore. Possimus excepturi maxime voluptas delectus facere vel. Quam
        repellendus eligendi distinctio magni cum fuga libero quos laborum, sit
        quas accusantium qui nemo, nostrum ut excepturi. Voluptatum corrupti
        nostrum velit, explicabo excepturi voluptatem consequuntur quos!
        Cupiditate ducimus adipisci dignissimos, ea quidem harum odio
        necessitatibus vitae exercitationem distinctio doloribus perspiciatis
        dolorem a illum corrupti natus non. Deserunt ducimus nihil ullam sed!
        Sit expedita animi nam voluptatum exercitationem accusantium debitis
        pariatur quis perspiciatis assumenda molestiae consequatur ad et
        quisquam doloribus odit, quaerat inventore provident ipsa. Odit, nostrum
        tenetur? Laboriosam nostrum eligendi mollitia ipsa reprehenderit nulla,
        pariatur necessitatibus quod aspernatur voluptas architecto, autem saepe
        nihil numquam quas expedita, ex deserunt excepturi incidunt ea. Commodi
        odit laudantium ipsum ducimus sed blanditiis eveniet. Molestias sint
        voluptate saepe architecto adipisci voluptatem quod ratione? Nobis unde
        odit ipsum illo officia assumenda, perferendis repellat reiciendis
        numquam libero labore nemo et. Esse eos minus saepe odit sapiente
        nostrum quo tenetur assumenda quidem iusto reprehenderit quam quibusdam
        voluptatum consectetur, praesentium sed mollitia ullam cum vel,
        temporibus beatae eligendi magnam omnis. Ut eaque expedita iste aliquid.
        Exercitationem, dolore nobis alias laborum saepe expedita ab provident
        unde repellat fugit a quos officia aut similique eligendi nemo, nihil,
        dolorum architecto. Omnis perferendis dignissimos non enim aliquid est,
        magnam accusamus, nihil error dolore laudantium voluptate. Iure, nihil
        officiis ad cumque assumenda iste mollitia. Possimus enim veniam earum,
        praesentium aliquam repellendus exercitationem culpa dicta modi
        deserunt, voluptas consequatur minus aliquid minima, asperiores maiores
        dolor dolore dolorum? Optio dolore nihil similique est incidunt pariatur
        saepe eligendi consequuntur maiores ea excepturi molestiae modi itaque
        neque vitae quia, animi aperiam dignissimos reiciendis laborum culpa at
        consectetur laboriosam. Excepturi nemo dolorum est, mollitia suscipit
        ipsum at deserunt itaque velit possimus quas, officia dolores eius
        veritatis laboriosam facere consequatur iure quisquam voluptatibus!
        Deserunt illum aperiam nisi numquam adipisci maiores doloribus quis
        quod, nobis cum itaque et nemo, ipsa architecto, repudiandae debitis non
        eaque explicabo id aspernatur? Optio, vitae ad nisi soluta iste
        repellendus. Aut incidunt aliquid laudantium impedit dolores, adipisci
        delectus veniam omnis soluta alias iusto illo saepe, dicta, aperiam
        molestiae harum ipsam. Voluptate sapiente perspiciatis adipisci
        cupiditate odit accusantium explicabo ratione molestias magni minima
        maiores earum aliquid, quasi labore voluptatibus beatae vitae, quaerat
        magnam. Nisi, amet? Dignissimos iste consectetur ducimus culpa quam
        illum quaerat cum rem, distinctio eveniet voluptate deserunt fugiat ad
        enim nostrum voluptates ut rerum. Et harum ducimus eius repellendus quo.
        Atque odit nulla officia deserunt vitae numquam obcaecati, voluptate
        cumque quo? Alias, ducimus? Error quam laborum qui ipsum atque.
        Doloremque, ad autem adipisci sed ipsa a quo, voluptatibus doloribus
        totam, impedit molestias unde non minus vero? Illum quidem nisi corrupti
        sint esse iure repellat eaque temporibus officiis, nostrum tempore alias
        unde earum suscipit. Rerum sunt nesciunt adipisci esse quod reiciendis
        at officia eius perferendis qui? Harum, rem voluptates. Voluptatum fugit
        sunt quos placeat repellat, minus, fugiat vel expedita ut debitis
        nesciunt voluptatem optio harum quisquam voluptatibus soluta, facere
        rem! Doloribus eveniet placeat voluptatum. Magni rerum inventore,
        cupiditate eum rem iusto! Esse, sed distinctio ipsum odit aspernatur
        pariatur dicta tempora tenetur ullam, fuga quibusdam iusto quia numquam
        modi. Perferendis veritatis consequuntur, dolorum provident, voluptatum
        culpa labore, placeat odit ea fugiat sunt dolores assumenda in quaerat
        deleniti cupiditate! Veniam, sed facilis modi accusantium minus dolores
        nemo quia quo officia fugiat, voluptatibus temporibus, explicabo dolorem
        consequatur laboriosam culpa ea amet cumque itaque porro assumenda
        doloremque vel! Consectetur, quis sapiente. Tempora quidem mollitia
        consequuntur ex optio molestias dicta temporibus repellendus, nulla
        laboriosam animi laudantium nesciunt ipsam recusandae repellat minus
        voluptates expedita ullam, quis veritatis ipsum aperiam officia aliquam
        fugiat! Aut perspiciatis doloribus repudiandae dignissimos natus, fuga
        quis possimus distinctio sequi atque blanditiis magnam, in delectus
        minima deserunt nihil at cum nesciunt saepe velit quae aspernatur? Harum
        sit, aperiam recusandae, dignissimos pariatur officiis velit voluptates
        non reprehenderit dolores deleniti ex corrupti exercitationem ab labore
        mollitia est quisquam ea nulla earum sapiente? Suscipit repellendus
        veritatis laboriosam dolorum tempora facilis eaque quibusdam quasi
        tenetur cumque corporis quam officiis aut possimus nulla magni,
        blanditiis maxime sed beatae pariatur culpa consequatur. Officia
        laborum, in blanditiis harum error ea expedita doloribus excepturi earum
        quidem corporis, eius impedit recusandae minus adipisci? Ipsum nemo
        unde, autem magni repellat, soluta eos nihil id consectetur adipisci
        officia quae iure repellendus, nulla temporibus quod placeat odit ea
        facilis? Facilis earum neque vel ipsam hic error odit consectetur illum
        explicabo in atque maxime quis velit reprehenderit odio corrupti, amet
        suscipit recusandae laboriosam non provident eaque beatae ipsum. A
        excepturi ab adipisci nam quos vitae animi, incidunt qui dignissimos
        atque quia soluta dolorem impedit! Inventore magnam laudantium officiis
        consectetur veritatis vitae id praesentium, quod harum, cum numquam
        minima. Consectetur nostrum aliquid asperiores alias libero eos aperiam
        quam velit mollitia facere officiis voluptate fuga dolorum illo in
        aliquam nihil optio est, explicabo fugiat iure perspiciatis dolorem.
        Voluptatem dolore consequatur, ducimus neque, in tenetur provident
        tempore obcaecati doloribus vitae vel omnis! Saepe expedita nemo enim
        vitae repellat accusantium, explicabo dicta ut eveniet repudiandae
        voluptate eum possimus ab necessitatibus ipsum laboriosam ipsam, rem,
        minus optio? Ipsa magni consectetur doloremque beatae ipsam itaque quod
        placeat id aut soluta, odio ea fuga architecto illum similique eaque
        minima saepe amet ullam eligendi aliquam sint odit? Reiciendis nobis
        autem amet voluptas perferendis vitae fugit qui exercitationem numquam
        totam ipsa quasi excepturi corrupti dolorem commodi soluta blanditiis,
        provident temporibus doloribus omnis odio animi quas consequuntur
        ratione. Soluta unde cupiditate molestias tenetur est earum obcaecati
        fugiat, necessitatibus fuga facere, dignissimos nulla repudiandae? Hic
        amet, neque dignissimos ratione repellat ad. Quaerat praesentium nam
        reiciendis eveniet mollitia aperiam, quisquam soluta omnis at illum.
        Quam explicabo, veniam alias, eos iure dolores fugit quidem, autem natus
        ea quisquam perspiciatis blanditiis atque dignissimos dolor non
        temporibus tempore unde. Molestias perferendis sint eaque ratione
        architecto, quia vero dolor, consequuntur excepturi quaerat placeat
        labore quas non voluptate animi tempora distinctio dicta dolorem iusto
        velit! Repellendus, facere, corporis error, magni id numquam mollitia et
        nostrum pariatur quia praesentium ipsam nobis porro. Illo ut fuga, porro
        officiis repellendus tempora explicabo atque ex error sit. Odio in
        accusamus quibusdam nulla perferendis cumque, voluptates facilis odit
        fugiat ea corrupti enim. Officia recusandae necessitatibus fugiat vel in
        tempore, maiores laborum eaque, quas delectus quibusdam earum magni
        vitae amet veniam quos labore commodi ab reprehenderit voluptates
        dignissimos! Voluptatem, quo recusandae iure voluptates incidunt
        deleniti exercitationem accusamus aliquam consectetur veritatis odio
        voluptatibus ut nulla in eligendi. Recusandae odit saepe, amet labore
        eligendi nostrum aliquid, blanditiis non vitae dolor commodi pariatur
        suscipit laborum sunt dicta aut rem eius unde tenetur nemo esse totam
        ab. Quis, hic quam non provident at totam ea quos laudantium impedit,
        dolore, quasi odio ducimus. Incidunt maiores corporis mollitia dolor
        accusamus consectetur, qui, ut saepe atque voluptates ratione eligendi a
        recusandae nostrum fugiat. Necessitatibus, maxime delectus ducimus
        deserunt quibusdam ipsum quisquam labore quam aperiam ullam magnam,
        architecto et, illo officiis laborum non est perferendis cupiditate
        repellat facilis quo rerum laudantium recusandae! Totam dolor harum
        sequi! Saepe itaque recusandae quae unde odio, expedita sed praesentium
        deleniti. Cum, quis. Quam beatae asperiores porro deserunt excepturi
        suscipit, reiciendis et dolorum tenetur commodi corporis voluptate, est,
        perspiciatis eius numquam delectus id incidunt impedit odio? Nam
        consectetur quod ipsam, ipsum adipisci autem. Laboriosam nostrum
        repellendus nesciunt saepe blanditiis dolore? Aspernatur, consequuntur
        esse porro vel cum iure modi optio repudiandae quasi officia, amet hic
        quam expedita nostrum itaque maxime in. Dicta quidem facere optio illo
        ad, ipsa veniam. Consequuntur, suscipit atque! Vero cumque maxime harum
        totam, perspiciatis numquam unde assumenda dolorum ipsam praesentium sit
        libero itaque? Quod consectetur corrupti aut alias perspiciatis impedit,
        pariatur doloribus dignissimos possimus saepe omnis libero illum fugiat
        deleniti eligendi dolore rem? Dolor magnam in culpa voluptatibus
        consequuntur ea sint quae explicabo inventore quis. Ut minima fugit
        aliquam totam dolorum quidem, optio doloribus, ipsum soluta incidunt
        explicabo maxime nobis dolorem eius, neque quisquam? Voluptate atque
        dolor delectus! Voluptatibus quibusdam dolorem sapiente quidem, fugit
        consequatur earum alias, obcaecati reprehenderit cumque saepe facilis
        aperiam. Cum aspernatur totam alias, repellendus recusandae laborum
        animi dolorum nihil dolor neque nobis tempora accusantium dolores maxime
        corporis praesentium itaque magni tempore inventore ea esse. Odio
        recusandae maxime exercitationem vero inventore beatae soluta aut
        tenetur, voluptate consequatur autem sequi debitis magni quos quas
        mollitia omnis amet nam veritatis corporis officia commodi? Delectus,
        fuga est. Minus ut deleniti officiis optio exercitationem libero odit
        fuga tenetur id eum veritatis, placeat, modi iusto architecto velit
        alias, tempore sed! Non assumenda deleniti suscipit sed nulla
        necessitatibus, dolorem repellat aspernatur vitae, dolores consequuntur
        odit dolor. Nulla sequi quaerat aperiam facilis officiis nostrum
        repellendus id ipsa eligendi omnis, atque libero saepe, doloribus velit
        natus voluptates alias iste sint! Itaque incidunt odit dicta aliquid
        provident explicabo! Quasi quos eveniet nesciunt rerum tempore ipsa
        veritatis labore quisquam neque reiciendis nam ipsam error ut soluta rem
        porro cumque maiores dolor fugit amet, vero doloremque harum unde. Illo
        dolor delectus magnam aliquam odit, enim libero minus asperiores
        officiis eligendi, corporis sit! Beatae, illum aliquid est rerum modi
        minima placeat iste aut illo asperiores voluptatibus iure enim officia
        nostrum molestias omnis voluptas sunt perferendis quia animi aliquam
        neque odio quibusdam sint. Iusto voluptatum, quaerat delectus labore in
        repudiandae quae laboriosam earum explicabo omnis facere odit possimus
        recusandae soluta non placeat, architecto eius? Culpa dolor cumque
        voluptates et voluptas iusto sit dolorem cupiditate saepe at quis cum
        atque eveniet voluptatibus quaerat, voluptatum accusamus ea eaque hic
        inventore suscipit? Provident, error pariatur libero, obcaecati placeat
        at sit, quia ut ipsam vero inventore. Perspiciatis quibusdam reiciendis
        nemo. Nisi quos ex ad debitis, quas officia. Suscipit magnam quisquam
        voluptas dolorem tenetur unde aspernatur sit repellat blanditiis nobis
        vitae laboriosam et itaque, accusamus laborum officia recusandae
        nesciunt porro cumque commodi veniam, officiis molestias illum eos. Et
        modi explicabo quam, recusandae dolores aperiam ea corrupti architecto
        odit repudiandae quis in animi quo eos ipsam deserunt sapiente atque
        eius ducimus accusantium nesciunt dicta. Amet tempora doloremque
        deleniti quas aut error, eum tenetur. Tenetur facere, consequatur ipsa
        unde velit consectetur repellendus aut amet quos quisquam quidem vero in
        repellat quae animi sit aspernatur cumque consequuntur iusto deserunt
        distinctio ducimus numquam? Aliquid, tempora officiis suscipit deleniti
        quidem reiciendis placeat earum esse natus molestiae voluptate ea
        nostrum explicabo nemo porro consequuntur ipsum officia saepe doloremque
        magnam impedit minus. Doloremque explicabo magni officiis laboriosam
        laborum architecto veniam eaque quam distinctio tempore! Delectus, illo.
        Et saepe perspiciatis dolores quo atque? Quo voluptatibus voluptates
        ratione eius perferendis quasi est? Odit necessitatibus, laboriosam
        temporibus quod vel repellat tempore minus eaque impedit eligendi
        aliquam sed, veniam, quia eos dolore saepe adipisci natus sint. Nam
        obcaecati, quod sit reprehenderit suscipit aut, repudiandae id unde iure
        ut maiores velit. Dolore similique dolorem dolorum eos nesciunt
        molestias, eaque expedita architecto nam distinctio eius quidem voluptas
        iusto impedit blanditiis ipsa delectus, ab laboriosam laborum aliquid
        quas. Consequuntur magni temporibus inventore optio voluptate vero
        veniam laboriosam distinctio ut officia quisquam suscipit maiores
        doloremque beatae aliquid, asperiores, soluta error perferendis quaerat
        saepe. In amet, expedita et aliquam, cupiditate deserunt ipsa laboriosam
        quidem eaque adipisci doloremque, provident itaque! Omnis vitae, aliquam
        cupiditate minus optio mollitia similique, nesciunt hic reiciendis autem
        eum. Ratione id consectetur molestiae fuga impedit adipisci quidem
        mollitia praesentium consequuntur animi expedita deserunt culpa,
        reiciendis eius provident soluta. Cupiditate repellat error possimus
        est, cum soluta adipisci modi illo velit? Porro natus dolores cum
        similique nisi temporibus dicta beatae quod autem atque sunt ad laborum,
        ratione voluptate culpa ea! Voluptate, veniam eaque quasi optio nobis,
        asperiores incidunt fugiat distinctio exercitationem ipsa magni
        repellendus debitis, nesciunt dicta vero. Voluptatum obcaecati
        necessitatibus rem quibusdam maiores eos nostrum saepe laborum, possimus
        praesentium ratione quidem doloribus aut et, eaque numquam dolore.
        Beatae tempore amet rem voluptatibus. Maiores magni praesentium id
        corporis quibusdam doloremque, officia commodi, cumque nisi doloribus
        repudiandae. Consequatur ut, officia sequi dolorem voluptatibus esse
        pariatur praesentium est maiores tenetur nobis ratione hic, laudantium
        eaque optio repellat non laboriosam dolorum modi aperiam dolor
        distinctio. Numquam iure quasi animi labore distinctio repellendus,
        deserunt ullam nesciunt quam, illum, qui corrupti corporis. Officia,
        dignissimos ea blanditiis saepe maiores modi dolorem commodi consectetur
        possimus odio sed iure? Eos nihil optio ea reprehenderit aperiam sint
        voluptates. Inventore neque tempora cum consequuntur obcaecati quasi
        exercitationem nulla temporibus nobis expedita architecto, impedit odio
        commodi dicta voluptate, quod laboriosam dolore reiciendis. Labore
        obcaecati quasi dolorem non ea alias, facere asperiores quaerat dolore
        quia? Odio qui delectus hic quod neque, minima doloribus, deleniti et
        totam, debitis provident cumque! Consequuntur illum fuga laboriosam
        dicta eum iusto veniam qui. Itaque sapiente iusto labore ipsum in, est
        accusantium hic ducimus. Obcaecati sapiente asperiores debitis delectus
        cum, quam veniam repellendus necessitatibus illo vitae ipsum hic.
        Suscipit vel voluptate voluptatibus sit totam similique in eaque quasi
        nihil non quas pariatur labore blanditiis provident consequuntur animi,
        nobis aliquam maxime ratione repellendus ullam quos consectetur
        inventore? Necessitatibus magnam commodi eos repudiandae labore sit
        voluptatem blanditiis iusto delectus eius atque rerum adipisci
        cupiditate ipsa itaque eum possimus, quia dolorem dolorum accusantium.
        Velit nisi adipisci enim quod esse pariatur quam modi temporibus sunt
        dolor obcaecati sed sit quo ab natus saepe repudiandae praesentium
        cupiditate laborum, quia nobis harum, necessitatibus itaque delectus!
        Ipsum cum voluptates deserunt quasi id vero incidunt alias consectetur
        maxime, quod similique sint eum, neque tempore delectus non veritatis?
        Quos, aliquam, nulla accusantium reprehenderit commodi odit praesentium
        ad beatae maiores dolores, ipsam velit impedit cumque iure consectetur
        fuga laborum? Molestias placeat saepe alias ex, consequatur cumque
        itaque enim autem maiores ullam sunt eos unde incidunt quam cum sequi
        quidem perspiciatis ut, mollitia dolorem? Inventore labore eligendi
        animi sint perferendis! Tenetur, a ipsam! Enim qui atque nostrum,
        facilis maiores officia doloremque, voluptatibus itaque vero, nisi ea
        sapiente ducimus eius perferendis aut aperiam recusandae repellat sint
        voluptates! Et accusamus dolorum, saepe quod placeat a est. Corrupti
        non, ex praesentium eum soluta consectetur mollitia quod tempore nemo in
        dignissimos illo, nobis facilis aperiam voluptas accusamus culpa magni
        dolorum quibusdam porro odio excepturi sunt cum quia? Accusantium
        nostrum temporibus ipsa nisi, veniam quas sequi quibusdam itaque iusto
        doloribus impedit officiis labore natus est id blanditiis expedita qui
        facere vel totam optio sint eum! Officia temporibus iusto quisquam
        soluta similique eligendi ex officiis, deserunt animi ad ratione totam.
        Quam mollitia perferendis, eum dolores maxime aperiam minus tempora
        obcaecati doloribus voluptatibus voluptate iste, reiciendis excepturi
        facere culpa possimus, animi cupiditate corporis sit labore? Fuga, quod
        commodi libero repudiandae nam tempora delectus omnis, similique totam
        ducimus suscipit provident sit hic earum accusantium voluptates aperiam.
        Nihil excepturi nostrum officiis? Magnam consequuntur nemo nulla. Animi
        eligendi voluptatibus earum ex voluptatum similique id reprehenderit,
        beatae dolore odit nihil in minus tempore quidem hic illum eos, nulla
        doloremque. Ipsam facere labore, quia tempore quis placeat blanditiis
        amet praesentium suscipit expedita quasi impedit, doloremque atque
        quibusdam totam? Perferendis asperiores officiis repellat nulla velit
        consequuntur iste sit optio deserunt error reprehenderit repellendus
        adipisci aliquid sunt ullam voluptatibus soluta beatae quis, voluptas
        corporis provident ea a. Sed mollitia temporibus cumque facilis ab
        ipsam, ratione explicabo, exercitationem dolor sint enim nemo in
        voluptates maxime magnam iste? Nisi sed vero eius totam nesciunt hic
        nostrum fugit minima, repudiandae molestiae harum et repellendus debitis
        ex officiis, ut consequatur, distinctio odio quo! Voluptatibus mollitia
        adipisci architecto eius asperiores nam quia accusantium labore sint ex
        omnis voluptas quidem doloremque, dolore ratione. Quia consequuntur
        nihil praesentium libero quaerat atque itaque perspiciatis expedita.
        Ipsum consequatur quibusdam minima. Expedita velit maxime doloremque
        neque quaerat dolor reprehenderit esse asperiores iure voluptas repellat
        et repellendus harum quos dolorem voluptates cum fuga alias eaque,
        possimus tenetur ex. Unde tempora fugiat quibusdam accusantium quis
        possimus non nobis incidunt soluta nisi amet harum reprehenderit vel
        odio accusamus, qui laboriosam quo optio. Voluptatem ullam pariatur
        exercitationem et sunt, obcaecati facilis dolore, eaque iusto magni
        nihil porro qui praesentium omnis, nostrum accusantium vel. Eaque
        consequatur sed reprehenderit error quod quisquam sint vitae perferendis
        numquam quasi pariatur, accusantium soluta quia, obcaecati dicta ipsum
        magnam neque amet ab perspiciatis, totam deserunt voluptatibus fugiat.
        Quisquam sed pariatur corrupti nisi, dolor eveniet. Iusto id in, magni
        eaque dolor culpa voluptate tempora quae quis fuga nulla maiores
        sapiente similique, a ipsum quam, autem corrupti corporis architecto.
        Consequatur explicabo odit suscipit neque recusandae adipisci voluptatum
        ipsum numquam voluptatem ducimus ratione, perferendis velit illum nobis
        repellat rem impedit unde error beatae enim nisi? Voluptas nulla
        repellat fuga est delectus rerum suscipit ipsa, dolorem corporis
        temporibus, dicta nobis quisquam minima fugit veritatis. Veritatis,
        nesciunt laborum? Inventore maxime nobis vel sequi explicabo repellat?
        Dolor ad sint molestiae eius maxime rerum excepturi distinctio nobis
        sunt? Officiis eveniet delectus, neque ipsum soluta, itaque commodi ab
        illum iure, nisi perspiciatis eligendi saepe nobis fugit! Doloribus
        similique atque consequatur iste suscipit non quis illo voluptate,
        debitis quaerat vel sit distinctio eveniet dolore praesentium ea unde
        consequuntur, hic quidem minima a aliquid, eligendi porro! Architecto
        possimus non laborum ab repudiandae modi expedita reprehenderit tenetur
        sint, tempore nam tempora fuga aspernatur corrupti ipsum dicta
        laudantium nulla iste officia? Ea minus voluptate, facilis ad quis harum
        dolore repellat, officia perspiciatis quo delectus sint sed error
        asperiores at cumque omnis rem quos. Accusamus sunt placeat sint
        corrupti magni modi, culpa minima, dolorem impedit dolore eaque repellat
        doloribus tempora dolores, ipsam quas reprehenderit voluptates ab odio
        maxime? Sed voluptas qui quae alias deserunt fugit accusamus optio esse
        iusto adipisci deleniti architecto fugiat, nostrum odio ab, enim
        voluptatum minus itaque. Rerum vel facere in omnis esse, consequuntur
        beatae doloremque, error minima rem placeat, cum voluptatibus dolor
        eligendi quam animi voluptas? Repudiandae porro aliquid totam! Nesciunt
        sapiente, velit molestiae totam impedit blanditiis atque facere magni
        quasi, deleniti, pariatur sit debitis eum recusandae porro sint? Eos
        accusantium et minus in soluta explicabo quas excepturi molestiae
        voluptatum culpa assumenda amet quos, quod maxime illum! Odit ex dicta,
        omnis laudantium nesciunt ab error nostrum aspernatur maxime, asperiores
        incidunt accusantium, saepe soluta veritatis beatae animi molestiae?
        Velit, exercitationem repudiandae ut itaque eveniet aut error eligendi
        magnam sunt tempora cum et corrupti possimus fugit! Animi, nam. Deserunt
        accusamus quae esse ut possimus recusandae quasi nulla quas rerum soluta
        architecto, minima facere corporis laboriosam illum nihil totam nam
        ipsum dolorem placeat voluptate consectetur reprehenderit. Recusandae
        dolore cupiditate porro perspiciatis quisquam, repudiandae placeat velit
        laborum laboriosam praesentium, quasi accusantium et sint provident ab.
        Voluptatem numquam quod voluptates deleniti eum omnis atque vel cum
        excepturi suscipit. Maxime voluptas necessitatibus excepturi
        voluptatibus accusamus odit veritatis at ut beatae? Esse libero odio
        repellat? Architecto labore enim sed perspiciatis temporibus. Ab quo
        itaque delectus repudiandae accusamus est illum laboriosam quia incidunt
        saepe. At nobis voluptas quibusdam ipsam harum iste, quas, nisi, aliquam
        autem ea sed nesciunt a? Minima maxime error voluptates earum fugiat at
        ad consequatur cupiditate fuga quo? A, minus cupiditate dolore
        asperiores vero repudiandae consequatur, officiis eaque illo ducimus
        omnis! Laborum eius neque doloremque possimus repellendus rerum, itaque
        maiores fugit culpa unde aspernatur ducimus aliquam eaque optio eligendi
        natus vel reiciendis in dolorem magni, similique qui dolores. Impedit
        sapiente molestiae suscipit earum. Asperiores fugit labore omnis non
        consectetur cupiditate, enim maiores voluptas, cum, minima ad esse!
        Inventore dolor adipisci commodi placeat non libero, doloremque
        consequatur veniam, culpa eius eaque quos quidem, accusamus assumenda
        vitae maxime. Commodi, unde et. Commodi voluptatibus magni fuga ex
        labore, itaque reiciendis sequi alias accusantium! Quia deserunt, non
        repudiandae doloremque nihil alias excepturi mollitia maiores saepe
        dolores voluptatibus eligendi. Modi deleniti doloremque provident
        inventore molestiae ex tempore commodi ab, rem id quisquam quas? Modi
        iure cumque repellendus quam placeat odio possimus exercitationem,
        voluptatem nemo vel amet corrupti doloremque. Sunt minus ea nulla
        incidunt. Exercitationem alias, ex dicta, placeat voluptas quam,
        adipisci quaerat illum cumque autem qui nesciunt beatae architecto
        magnam commodi quisquam eaque aut distinctio? Odit quidem alias corrupti
        assumenda nobis veniam placeat fugit nulla aliquam deserunt nesciunt
        laudantium, enim illum sed iusto in maiores corporis possimus officiis
        id odio dolor quam. Et exercitationem eveniet eaque quas officia
        suscipit magni, ad sit dignissimos, animi voluptatem saepe fugit numquam
        sequi hic voluptate nemo maxime. Vero neque voluptatum exercitationem
        officia sed ipsa in voluptatem sunt iusto incidunt optio nostrum
        molestiae deserunt iste dolor, nisi cupiditate odio modi voluptates, ab
        vitae. Ducimus voluptate eligendi expedita, soluta fugit esse nesciunt
        accusamus repellendus vitae est! Consectetur dolorum eveniet quod
        corporis magni, consequuntur atque reprehenderit! Quidem cum
        exercitationem similique ut asperiores est nesciunt deleniti vero, fuga
        vitae nostrum excepturi saepe a ad rerum consectetur nihil voluptate
        modi distinctio aut iure minus? Commodi porro vero sequi quisquam. Natus
        est maxime voluptates magni excepturi labore et atque mollitia expedita
        beatae aliquid adipisci accusantium voluptate iste sint necessitatibus
        dicta, voluptatem, ipsam molestiae repellat amet. Eum nostrum, excepturi
        voluptatibus exercitationem architecto ab explicabo praesentium
        perspiciatis saepe enim iure ad! Autem maxime earum ex quidem officiis
        rerum unde sunt, tenetur voluptatem corrupti facere placeat non nemo aut
        eius quibusdam commodi porro consequatur eos et ducimus a? Error
        aspernatur nam suscipit assumenda, numquam sed molestiae eos doloremque
        labore, ipsam corporis at. Odio obcaecati consequuntur ducimus
        consequatur, dolorem ipsa culpa dicta officia nihil ab reiciendis at
        veritatis laboriosam illum facilis quos? Voluptatem dolore ab omnis
        suscipit. Perspiciatis cumque et minus qui labore similique suscipit
        assumenda neque asperiores voluptas quam, quis maiores voluptatem, in
        optio repellat? Dolore hic id maxime officiis voluptate vel itaque
        voluptatem, repellat soluta similique aperiam nisi? Obcaecati
        necessitatibus officiis eaque nihil accusantium officia doloribus eos ea
        placeat, neque commodi at expedita. Sapiente eos modi facilis assumenda
        aspernatur, consectetur eveniet quis commodi error amet eligendi debitis
        saepe in iure similique fuga labore odit illo vel omnis, dolore adipisci
        quaerat quos aut. Ratione, voluptas corporis nesciunt in quae minima
        perspiciatis architecto commodi vel illo at doloribus natus earum
        eligendi tenetur autem quasi a vitae soluta tempore nihil. Deleniti
        impedit ea adipisci minima, omnis error at blanditiis porro ipsa quidem
        facere ut ex reprehenderit beatae distinctio enim numquam ipsam dolorem
        nisi. Cumque vitae neque vero similique alias, placeat nisi cum eos
        veritatis quae adipisci necessitatibus eligendi! Molestias sequi ipsum
        consequatur non est inventore. Placeat cumque amet nihil, quam
        blanditiis laboriosam odio quas officia ipsa eum officiis quaerat. Qui
        aliquam voluptates laboriosam vel earum aliquid cupiditate explicabo
        tempora nihil minus sed excepturi reiciendis assumenda repellendus
        incidunt deserunt facere, tenetur obcaecati ipsum temporibus maiores
        suscipit iure nisi iusto? Harum magni recusandae eius repellendus rem
        blanditiis impedit dicta fuga obcaecati ex vero tempore reiciendis
        possimus, ab cumque minus, veniam velit saepe quo sed dolor at hic sint
        natus? Esse, repellat delectus ad laboriosam ex assumenda doloribus
        veritatis voluptas! Cum animi exercitationem omnis quam, quo quaerat
        commodi suscipit? Molestias fuga molestiae aperiam recusandae, nihil
        sint impedit repudiandae doloribus sapiente ratione voluptas illum
        inventore eum laboriosam enim mollitia, quia quidem sequi neque ex
        adipisci alias ipsum vero. Praesentium maxime expedita quibusdam dicta.
        Quaerat voluptatibus velit itaque, cupiditate porro omnis nesciunt
        suscipit ex labore nobis rerum beatae asperiores cum nulla perspiciatis
        quo ullam! Sed commodi officia non numquam obcaecati, consequuntur
        labore laudantium beatae sequi rem ab. Tenetur excepturi nihil, a eos
        eius mollitia eum libero! Accusantium perspiciatis placeat distinctio,
        doloremque at incidunt iure alias repudiandae atque nisi pariatur omnis
        nam sed quis ipsam dignissimos est adipisci maxime quaerat nobis eaque
        reiciendis commodi error voluptatibus? Iure a, harum perferendis id vero
        iste labore culpa? Quam tenetur ipsam mollitia rerum eius dolor soluta,
        corrupti est dolorum repudiandae atque quod. Voluptas omnis error
        impedit mollitia quae nihil nulla animi, provident cupiditate illo autem
        quisquam accusantium laudantium atque voluptatibus natus iusto
        asperiores nemo possimus ut deleniti veniam accusamus, quos esse.
        Repudiandae temporibus quidem architecto repellendus dignissimos hic
        quaerat aperiam debitis nostrum tenetur optio, repellat nisi dolorum
        cumque nobis! Sit recusandae, ipsam autem placeat suscipit fugiat
        necessitatibus amet cumque mollitia inventore, molestias ducimus
        molestiae numquam libero! Odio tenetur voluptatibus id aliquid, optio
        et! Nihil incidunt, id obcaecati similique, maiores dignissimos nobis
        dolores perferendis nostrum officia esse. Assumenda exercitationem animi
        dolorem veniam sequi odio, corrupti obcaecati nemo vero nostrum
        praesentium nesciunt cumque necessitatibus libero cum provident id
        cupiditate velit tempora eligendi sed maxime! Itaque dolorem maiores
        magnam hic explicabo repudiandae inventore incidunt, quo repellendus,
        ipsa maxime corporis voluptates corrupti amet! Quae nihil commodi
        perferendis natus quidem libero nobis fuga iure accusamus porro alias
        facilis fugiat numquam rerum, inventore dolorum adipisci molestiae earum
        omnis, velit quaerat cumque. Distinctio voluptatum natus hic excepturi
        eos numquam necessitatibus delectus non, eveniet incidunt quidem nobis
        consequuntur perferendis, earum nemo est! Nihil repellat labore
        veritatis, quam architecto aut accusantium provident ut aspernatur
        recusandae, dolorum asperiores explicabo. Assumenda fugit magnam
        consectetur non beatae maxime quidem est accusamus perspiciatis libero
        earum, ducimus alias sint dicta, quis nemo maiores facilis velit
        repellat odit! Vel, itaque. Eaque rem sunt architecto sint magni minus
        blanditiis molestiae provident. Sit beatae commodi, ratione blanditiis,
        rerum distinctio nisi consequuntur harum natus maxime numquam sunt
        repudiandae at! Officia libero, explicabo, perferendis adipisci
        molestias accusantium harum quisquam nesciunt repellendus quibusdam
        facere. Optio quaerat rerum, labore similique cupiditate in a. Eum
        tempore, officia, ipsam impedit quae recusandae, quia reiciendis et
        dolor rerum veritatis voluptate hic magni cum. Totam animi
        necessitatibus possimus adipisci praesentium rerum, quas, neque,
        doloribus fuga blanditiis laboriosam nulla quos sapiente repudiandae
        harum quam. Inventore qui libero ea eligendi nemo, aliquid laboriosam
        consectetur sapiente ullam ipsam fugit illo tempora nesciunt nulla rerum
        distinctio, dolores asperiores delectus deleniti aspernatur, voluptatum
        blanditiis vel nostrum. Ad reprehenderit vel natus atque et nobis velit
        itaque voluptates distinctio quos, numquam esse harum aliquam maxime
        corporis, quisquam quam nam provident. Impedit facilis, repudiandae
        earum ducimus enim fuga reiciendis cumque? Doloribus nobis officia nulla
        non quis mollitia necessitatibus porro ut fugit quos rerum, amet quasi
        excepturi aspernatur. Delectus ut numquam repellendus quam amet ad quasi
        labore voluptatum facere fugiat laborum ab aliquid ullam aliquam neque
        cupiditate suscipit incidunt nostrum velit, id, officia, commodi
        impedit! Aut, recusandae sequi! Veniam eveniet totam nulla quis facere
        adipisci dolorum ab facilis commodi. Et consequatur dignissimos optio
        illo perspiciatis? Quidem pariatur quibusdam aliquid eveniet eaque
        exercitationem qui debitis temporibus dolorem consectetur maiores
        tenetur quia neque voluptatum, voluptatem veniam libero asperiores
        accusamus culpa officiis. Distinctio, tenetur voluptate excepturi unde
        nobis odio assumenda tempora quos sapiente veniam nulla eum quia
        suscipit laboriosam? Ut facere quidem ad nemo officiis, vel recusandae!
        Eveniet accusantium inventore dignissimos minima rerum incidunt. Sequi,
        odit ad. Illo odit officia accusamus iusto, corporis recusandae
        consequatur nam voluptatibus. Cupiditate dolorum corrupti magni odit
        provident aliquam molestiae autem eos minima non itaque consequatur
        fugiat, deleniti eaque dignissimos. Iste, corporis impedit! Numquam
        laboriosam facilis fugiat laborum voluptatum, modi ratione, sint ea
        soluta nihil dolores. Ex possimus odio nihil libero quia. Iste
        praesentium suscipit, vel rem officia, dicta amet at sunt minus quod
        iusto consectetur eum reprehenderit quas quae saepe nulla velit error,
        adipisci explicabo minima ullam incidunt! Nisi, ipsum. Repellendus, ab
        culpa. Eaque tempore saepe suscipit provident non, officiis molestias
        dolore dolores est ratione praesentium ea officia. Eaque soluta non ab
        deleniti, fuga possimus et illo necessitatibus nemo tempore ipsam
        voluptatem eveniet odit dolorum nobis assumenda. Ullam accusantium,
        reiciendis eaque totam autem deserunt? Iste laboriosam obcaecati enim
        sint fugit beatae facilis minus quaerat sunt! Facilis commodi sint
        impedit praesentium cupiditate? Corrupti odit sit consequuntur
        quibusdam, atque omnis molestiae. Tempora vero nihil suscipit corporis
        unde atque quas cumque molestiae labore expedita quam, recusandae
        veritatis. Ipsa nam nobis blanditiis quas placeat fugiat nulla neque
        vitae eos adipisci ut incidunt in magnam commodi, nostrum hic animi unde
        dolorem perferendis corporis, aspernatur veniam ratione est voluptatem.
        Doloribus numquam maiores saepe, deserunt architecto a aspernatur dolore
        optio necessitatibus totam neque explicabo! Odit suscipit distinctio
        voluptates, tempora a vel modi, enim praesentium beatae unde ad eius.
        Deleniti laudantium error possimus quas. Labore aliquid nesciunt libero,
        eveniet eius praesentium dolore, sunt placeat autem, maxime culpa
        eligendi. Accusantium repellendus eveniet praesentium illum magni
        recusandae adipisci voluptatibus. Tempora illum consequatur provident at
        magni rerum voluptatem mollitia eos! Saepe atque totam commodi eos quam,
        quasi accusamus exercitationem quod odio voluptatibus! Ea in enim quo
        nihil ipsa. Ex amet sapiente nostrum aliquam quibusdam! Ut aliquam
        ratione cupiditate perspiciatis recusandae quia ad. Corporis hic eveniet
        qui illum fuga deserunt atque veritatis quisquam? Est quidem voluptates
        eveniet necessitatibus iste asperiores ipsam molestiae ab debitis ea
        beatae ad reprehenderit earum harum aliquid sed, tempore recusandae
        praesentium veritatis rerum maxime provident aliquam similique
        blanditiis. Iusto, repellendus modi! Dignissimos ex quo officia
        laudantium iste mollitia aliquid magni in autem, enim ullam modi fugiat
        vitae possimus atque iure, cumque laboriosam nisi ducimus consequuntur
        delectus incidunt sed molestiae quod! Officiis enim eaque alias
        obcaecati, voluptas doloremque repellat voluptatum voluptates sit
        eveniet et reiciendis magni quaerat officia ad fuga doloribus deleniti
        culpa quasi facere quia tempore. Eveniet obcaecati illo, aut soluta
        deleniti doloribus odio nulla nisi sint aspernatur. Eaque in ducimus
        sequi cumque error vitae maxime, doloribus, temporibus repellendus
        aliquam est aperiam sit neque numquam rerum voluptates iure ex
        consequuntur quisquam veniam? Fugiat a tempore ab nostrum voluptate eius
        asperiores quibusdam unde, quia officiis dolorem consectetur eum
        explicabo numquam quod distinctio ullam minima, aut incidunt fuga! Enim
        consequatur explicabo nostrum. Distinctio deleniti possimus aperiam fuga
        esse aliquam sequi minus. Itaque voluptates quod quasi nobis magni,
        totam qui eveniet ad neque minus, error molestiae expedita consequuntur.
        Unde velit nulla magni modi hic distinctio. Dolores exercitationem, sint
        est reiciendis quidem facere odit deserunt, libero perferendis
        recusandae ut amet voluptatibus laborum quo quae quisquam labore, id
        incidunt quas sit minus consequatur harum. Commodi, voluptate? Delectus
        nam inventore cumque in iste quaerat eos soluta! Obcaecati, sapiente
        quod minus fugit magnam corrupti consequatur adipisci rerum! Repellat,
        architecto sit! Ducimus, esse? Quia asperiores aliquam odio? Est fuga ut
        provident delectus eius nesciunt aliquam veritatis. Quibusdam, provident
        quos delectus corporis assumenda ratione eligendi, exercitationem fugit
        modi excepturi iure nemo commodi sapiente beatae? Nobis, sit beatae?
        Voluptates quibusdam nemo pariatur ipsa esse, quos sint laboriosam ipsam
        officiis rerum alias sapiente neque, sed a? Consequuntur iusto
        asperiores reiciendis illo quisquam, similique expedita eaque omnis
        provident voluptatibus doloremque, temporibus libero consectetur, neque
        sint adipisci? Voluptatibus omnis ex inventore maxime fugiat amet ipsam
        quia veritatis corporis laboriosam iste earum nihil in adipisci dolor,
        reprehenderit quisquam temporibus mollitia ut autem exercitationem ea!
        Alias aperiam, esse magni perspiciatis illum dolores fugit accusamus,
        veritatis officiis dolorem reiciendis temporibus tenetur molestiae quis
        qui voluptatibus labore quod molestias? Consequuntur laboriosam
        explicabo neque accusamus illo sed blanditiis autem, qui, voluptatem
        molestiae, possimus tempora similique impedit repellendus vel veniam
        rerum? Consectetur recusandae eaque consequatur sed repellat et sapiente
        atque sunt, reprehenderit quibusdam, modi ducimus quo praesentium ad
        exercitationem natus vitae expedita vero. Culpa vitae animi corrupti
        ducimus aliquam? Consectetur accusantium, tenetur vitae, in deleniti
        veritatis similique sunt mollitia non quo cupiditate hic laborum itaque
        a, laudantium aliquam fugit dolorum assumenda beatae vel. Ab ducimus
        necessitatibus voluptates reprehenderit alias aliquid error eligendi,
        odio consectetur fugit eos et debitis. Temporibus, corporis. Ab dolor
        asperiores quos perspiciatis, impedit alias nam ipsa, eum, ipsam
        blanditiis cum qui dignissimos reiciendis eligendi deleniti earum
        delectus a. Illum minus, pariatur quisquam cum nisi esse beatae, animi
        error repellat possimus reiciendis. Culpa voluptatibus odit dolorum
        voluptatem quaerat accusantium nisi fuga facere. Repudiandae tempore,
        eaque dolor corrupti officia ratione tenetur adipisci minima, architecto
        commodi ducimus nulla qui ipsa quis impedit iste odio numquam dicta.
        Vero id optio natus nobis unde eius, ullam assumenda, molestiae ea quos
        soluta saepe, itaque similique sit inventore illo sapiente! Eaque, minus
        et? Reprehenderit laborum beatae reiciendis consectetur ea enim. Odio
        earum magni non itaque perferendis expedita molestiae, accusamus
        dignissimos! Voluptatem omnis eaque quibusdam atque! Odio molestiae
        dicta saepe dolor maiores ullam esse excepturi similique, sit rerum
        aspernatur illum itaque consectetur consequuntur pariatur cum laudantium
        totam nemo veritatis reiciendis. Similique est, velit delectus assumenda
        dignissimos nemo obcaecati explicabo sed ullam magni officia unde omnis
        vero expedita voluptatum. Nesciunt ullam obcaecati eligendi voluptatum
        vero iste doloribus debitis, exercitationem at est veritatis vel
        doloremque perferendis vitae adipisci provident quam accusamus nemo
        alias non numquam nulla tempore facilis? Nulla veniam explicabo mollitia
        necessitatibus ut, iure placeat, pariatur eos, ducimus dicta dolores
        consectetur. Praesentium assumenda in, nemo saepe magnam ducimus rem
        quia veritatis, blanditiis veniam similique molestiae neque est expedita
        fugiat, quaerat quidem aspernatur non reprehenderit! Neque error
        necessitatibus dolores! Minus impedit dolorem corrupti voluptatum
        laborum temporibus, eaque sint! Qui, officiis. Voluptate asperiores
        doloribus beatae error culpa debitis ut, qui non. Delectus, earum
        repellendus corrupti dolorum aliquam magni ipsa culpa harum corporis sit
        repellat natus eum reprehenderit eaque placeat dolore sunt fugiat
        molestiae quisquam accusantium voluptatem laboriosam quos? Dignissimos
        maiores repudiandae facilis nihil quae ad modi placeat labore deserunt
        obcaecati, perferendis quidem impedit eum sit possimus quibusdam. Ullam
        nemo repudiandae hic reprehenderit, dignissimos blanditiis molestias
        nesciunt id earum fugit similique eos laborum vel nam soluta minus
        assumenda? Non illum assumenda ipsum, praesentium quo ullam? Iure unde
        earum deserunt officiis temporibus ratione expedita illo ipsum enim
        vitae quod facilis laborum sed necessitatibus perspiciatis, explicabo
        quia? Laboriosam quibusdam nisi fugit esse ducimus eligendi magnam dicta
        assumenda saepe, incidunt ad sint temporibus architecto in ipsum modi ab
        a nam officiis, unde quia? Repudiandae animi quos repellendus.
        Repellendus aliquid aspernatur sed voluptates at! Eius beatae, quam
        culpa vel quod consectetur, accusantium magni nam ipsum ut dicta
        quibusdam aliquam, at illo commodi repellat assumenda ad incidunt. Quos
        facere dolorem odit explicabo, blanditiis natus porro accusamus vero
        ullam totam. Nihil quasi quos id sapiente nulla vel aliquid, consectetur
        in ea quisquam voluptate voluptatem autem sunt dolor incidunt doloremque
        mollitia reprehenderit adipisci ut, blanditiis fuga, quam nisi qui
        consequatur. Recusandae eveniet perferendis quam sint cumque vel veniam
        debitis, nobis, unde dignissimos nesciunt quae laborum sed inventore
        perspiciatis dolores ipsam veritatis! Sunt vero laboriosam reprehenderit
        porro veritatis. Autem animi illo molestiae fugiat neque eligendi
        veritatis nostrum numquam commodi quasi repudiandae voluptate explicabo
        id vero illum quidem, est temporibus aut veniam ipsam debitis alias ea?
        Dolores accusantium incidunt odit adipisci illo placeat necessitatibus!
        Eaque aliquid nulla neque iure veniam, perferendis voluptates vero.
        Expedita animi quidem corrupti asperiores. Suscipit iusto nam dicta
        veritatis ut nulla, eum maxime nihil qui modi similique veniam. Fuga
        maxime aliquam ut. Nesciunt quos aut molestiae, iusto distinctio id
        optio repellat ab nostrum quas nemo fugit facere ipsa cupiditate magnam
        fugiat sit quis quisquam rem libero mollitia voluptatem! Quasi assumenda
        illum, quam autem dicta eaque quo fugit explicabo! Dolorem explicabo
        consectetur molestiae quaerat corporis, obcaecati, iste omnis
        accusantium asperiores voluptatum autem reiciendis unde atque expedita
        voluptates! Nam voluptates quidem numquam magni? Asperiores pariatur
        error eveniet ea ab unde sit, officiis minima vero odio excepturi harum
        molestiae inventore fuga repudiandae saepe commodi labore ex dolorem
        voluptate. Esse nesciunt, cum obcaecati quibusdam tenetur veniam rerum
        velit, temporibus excepturi necessitatibus soluta earum neque debitis
        molestias error vitae ab adipisci corporis! Dolore labore numquam itaque
        voluptates quia facere facilis ratione, officiis voluptatem sint eius
        incidunt reprehenderit magnam libero voluptas quasi. Libero assumenda
        voluptate officia voluptatum odit illo eaque corporis, repellat
        consectetur praesentium placeat? Quos molestiae ab, quidem aliquid
        nesciunt fuga placeat, laudantium porro eveniet consequuntur voluptatem
        facilis commodi suscipit? In repudiandae aut harum impedit amet
        asperiores veritatis ullam, illo labore commodi itaque, ut natus veniam
        fugiat fugit unde ratione obcaecati iusto magnam? Ipsam sapiente ad
        consequatur ab cum magnam in dolor a ex, voluptatum minima? Temporibus
        quaerat, excepturi et ex vitae deserunt ipsa, earum, aspernatur maxime
        quas ipsum ut eaque ipsam laborum consequuntur aperiam reiciendis. Ipsum
        sit itaque qui obcaecati maiores sed nostrum quia. Excepturi nam
        architecto nostrum eius ab cumque! A earum quidem, atque temporibus
        aperiam deserunt esse excepturi magnam sed expedita, consequuntur
        nesciunt quos numquam adipisci error repellat non debitis tempora
        aliquam dignissimos. Iure consectetur alias eaque deserunt dicta ipsa
        voluptatum, aut architecto veritatis optio harum, facilis magni quos
        molestias quas? Totam quis maxime nobis nam saepe et iste, iure sequi
        explicabo ipsa tempora itaque. Ut nemo sapiente veniam nobis ea sit
        quidem suscipit ipsam quo aperiam aut perspiciatis tempora minus ad quae
        dicta quaerat fuga repellat doloribus sequi, magnam, asperiores maiores?
        Sed dicta explicabo, sapiente expedita pariatur laboriosam veritatis
        eaque possimus dolorem eius! Praesentium, iure dignissimos? Beatae, qui
        ratione! A mollitia assumenda quia temporibus quaerat quasi dignissimos
        dolorem id, harum deserunt. Cum porro, iste expedita a suscipit quas
        itaque voluptatem quis rerum fugit nisi, at magni omnis qui deleniti ea
        aliquid laudantium eius officiis corrupti consequuntur earum nihil?
        Officiis temporibus est nobis ratione fuga sunt repellendus neque sint
        molestiae repudiandae pariatur excepturi eveniet similique aspernatur
        totam placeat consequatur inventore eius omnis, cupiditate laudantium
        voluptas, error nihil aliquid? Debitis aspernatur facere sapiente
        cupiditate, soluta mollitia quisquam, excepturi, ex molestiae quas
        voluptas. Provident nihil pariatur aspernatur vel architecto facilis
        modi, quasi numquam exercitationem praesentium, fugiat error commodi,
        saepe sapiente quam debitis autem recusandae dicta. Voluptate reiciendis
        omnis explicabo, adipisci quisquam unde quidem aperiam nobis beatae
        officiis inventore, quos reprehenderit dolorum, earum assumenda?
        Cupiditate, doloribus voluptate necessitatibus vitae voluptatum dicta
        dolorum exercitationem ex magnam nulla inventore eos autem impedit totam
        qui et atque commodi cum eius libero ratione debitis? In dignissimos
        obcaecati a porro quaerat, doloremque excepturi odit provident,
        cupiditate facere esse praesentium voluptatem eveniet sed veniam
        doloribus quae aliquam libero fugit deleniti placeat voluptatibus. Quia
        inventore nulla vero reprehenderit enim omnis necessitatibus unde,
        beatae, mollitia natus ratione consequuntur eveniet optio perferendis,
        minima dolor. Beatae et ullam, rem minus dolor consectetur cum magni
        explicabo distinctio enim! Natus nostrum ut molestias explicabo unde
        quasi exercitationem. Nisi aliquam magni recusandae labore et, autem
        iusto exercitationem laborum perferendis voluptas eaque repudiandae
        debitis reiciendis natus nam eius quaerat odit vero consequatur corporis
        architecto inventore sed similique quia? Laborum repellat tempora quo
        libero maiores magni qui iusto molestiae ex et, dignissimos nobis atque
        exercitationem? Incidunt velit pariatur aliquam officiis dolore minus
        excepturi blanditiis quasi. Velit, deleniti iusto nulla impedit libero
        rerum aperiam, distinctio optio tempore repellendus vero accusamus
        doloremque saepe ea corrupti ut corporis, placeat architecto suscipit!
        Voluptatibus id, sint architecto ut velit sit, minus tempora quia
        incidunt, obcaecati quam enim dignissimos! Quisquam, ad quaerat
        architecto aut illum eligendi, mollitia deleniti recusandae culpa
        aspernatur unde accusantium assumenda non inventore debitis? Repellat
        delectus quas commodi, nostrum facere sed ipsum architecto quo facilis
        molestiae quidem vel eligendi molestias, quasi vero quos necessitatibus
        tenetur labore repellendus? Laboriosam eos mollitia, voluptate libero
        dicta consectetur necessitatibus sapiente numquam porro? Itaque, quia
        officia obcaecati quod nulla minima? Possimus fugiat commodi sequi in
        eius ut molestias expedita veritatis fugit hic incidunt quae cum
        dolorem, ipsum pariatur natus qui? Ratione officiis sint, adipisci ut
        error perspiciatis debitis nemo minima! Aspernatur rerum iure totam.
        Fugit debitis corporis ab non quaerat vel voluptatum pariatur modi hic,
        quasi eum a, esse at autem quisquam quia tempore sequi nemo amet maiores
        id. Fuga eligendi voluptatem quibusdam mollitia provident, eos debitis
        optio, consequuntur harum repellendus eaque omnis quasi ullam expedita
        facere earum dicta quo sunt recusandae. Tempora, sequi perspiciatis.
        Eveniet, labore modi, ut ullam pariatur aut dignissimos fugiat quas ab
        vitae sunt? Tempora, et atque, delectus nam quasi suscipit consectetur
        voluptatum harum optio officiis dicta eligendi ullam quae quo illo, esse
        beatae vitae obcaecati? Eius nostrum at vitae, incidunt id dolore sequi
        dicta error placeat commodi, accusantium voluptate quibusdam veniam
        ipsum, vero doloremque corporis iure ipsam ratione itaque in ducimus sit
        aliquid. Quidem eius error repudiandae harum repellat consequatur est
        odit! Facere, eligendi. Facere voluptatem vel adipisci, distinctio
        minima odit ipsa atque voluptate. Necessitatibus quam accusantium cumque
        ipsum assumenda neque aspernatur, aliquid, nobis rerum id natus
        asperiores voluptatibus doloremque ullam! Consequuntur consectetur eos
        illo, laboriosam dolor maiores sapiente ipsam quibusdam saepe, earum id!
        Qui blanditiis cumque dicta laudantium laboriosam eaque tenetur ipsa,
        officia iste cum omnis itaque, exercitationem sint est molestiae
        nesciunt sed laborum inventore nihil assumenda! Debitis natus explicabo
        neque odit perspiciatis excepturi corporis consequatur, voluptatibus
        sint voluptate animi reiciendis sit, minima quibusdam alias autem labore
        vitae odio dolorum totam qui blanditiis, nemo velit eaque! Saepe atque
        cupiditate rem laudantium quam, voluptas amet pariatur voluptate ipsam
        assumenda consectetur porro numquam, deserunt debitis eaque vitae eius
        animi? Quidem cumque impedit non similique soluta optio blanditiis amet
        ipsa ratione eum repudiandae, accusamus atque delectus commodi
        reprehenderit voluptate rerum aliquid odio laudantium? Vero beatae neque
        laudantium ipsum pariatur delectus itaque natus doloremque quia, dolorem
        odit est minima voluptatibus atque, non deleniti nihil aperiam
        consequuntur vel. Nobis earum nisi asperiores, fuga quis, nam doloribus
        atque cum neque, tempora voluptate fugiat? Aliquid, officia. Eveniet
        quis voluptates earum aspernatur eum aut mollitia, dolores ex corrupti
        incidunt vitae velit explicabo animi voluptatem tempore? Libero
        explicabo harum modi id officiis quo quas incidunt, at odio cum
        voluptates quos voluptas velit ea. Magni necessitatibus nulla ullam
        omnis praesentium officiis. A consequuntur iusto eos nobis cumque iste
        itaque molestiae maxime atque amet officiis molestias quis tempore
        voluptates, quia ipsa aperiam at eaque praesentium aut enim. Voluptate
        laboriosam rem aut porro consectetur officia! Nisi, culpa sed atque
        autem aperiam accusamus quos, neque officia saepe corrupti repellendus
        impedit est quis recusandae. Exercitationem suscipit rem iusto ipsam
        eveniet, adipisci blanditiis ducimus quos ullam non iste vitae
        dignissimos voluptatem. Sapiente ullam libero, delectus quia nostrum sed
        perspiciatis quos ut vero. Optio nostrum magnam nisi! Maiores
        praesentium minima cupiditate consequuntur dolorem blanditiis alias
        officia quod ex quisquam dicta eius neque, nihil debitis possimus omnis
        sit beatae itaque in optio architecto saepe reiciendis? Mollitia
        pariatur dignissimos porro, odio minima magni nihil quo reiciendis
        eligendi doloribus iusto unde amet fugiat veritatis fuga natus
        laudantium recusandae molestiae sed itaque, in aliquam! Necessitatibus
        impedit itaque temporibus fugit cupiditate, ullam sed soluta. Obcaecati
        modi voluptatibus odio magni est. Facilis, possimus, aut dolores fugit
        delectus quos distinctio laudantium id vero optio eaque omnis earum
        incidunt libero quae autem, non cum ea et? Aliquam perspiciatis eius et,
        quam modi omnis magnam officiis nulla totam adipisci nobis minima dolor
        consectetur consequuntur aliquid. Commodi, delectus dolore veritatis
        nisi quae unde repudiandae animi fuga neque accusantium error, deleniti
        assumenda cumque cupiditate totam ipsam alias aspernatur quia earum
        tenetur et! Dicta necessitatibus quos natus aliquam possimus incidunt,
        animi aspernatur nobis repellat hic repellendus voluptatibus, doloribus
        rem quod pariatur id non, neque eaque voluptatem! Laboriosam soluta
        incidunt quaerat ut velit repellat ea quam. Qui, dicta sint. Consequatur
        assumenda, rerum quos sapiente excepturi odio accusamus provident nobis
        eaque adipisci sunt repellat odit beatae perspiciatis tempore quia,
        neque nesciunt. Placeat aperiam maxime sed veritatis? Aut eius
        doloremque expedita, culpa velit repellendus blanditiis? At quibusdam
        quisquam dolorem rerum quas omnis necessitatibus. Ducimus obcaecati ex
        iusto illo eaque, libero qui nihil, molestiae id voluptas rerum dolor.
        Eveniet quidem incidunt, rem tempore facilis omnis repudiandae vel
        molestiae ad hic praesentium a eos porro minus ipsam ex magni accusamus
        recusandae debitis vitae? Libero nam totam non culpa quod magnam, esse
        repellendus similique laborum doloribus! Odit, veritatis vero dolorum
        magni repellat recusandae non consectetur cupiditate ex cumque,
        laboriosam quod ab quis amet, voluptatum similique minima expedita
        ducimus exercitationem voluptatibus reprehenderit? Unde labore rem,
        laboriosam quam non necessitatibus expedita dolorum fuga perferendis
        illo! A sed ex cumque libero impedit similique corporis aspernatur
        numquam vel? Recusandae voluptatem ut non laudantium numquam aperiam,
        corporis sapiente consectetur iure, sint culpa tempora, qui quae et.
        Accusamus eos maxime at ipsum soluta dolorem maiores quasi aut aliquam
        beatae, ducimus deserunt animi, libero placeat? Pariatur at nemo tempora
        sed, quibusdam quos in incidunt iusto, cupiditate labore dolores
        architecto eveniet libero non, placeat aliquid sit dolor minus eaque ad
        adipisci ex repudiandae. Pariatur consequatur, alias deserunt blanditiis
        optio ipsa error qui excepturi commodi minus suscipit fuga, eum
        architecto dolorum quasi ullam debitis nesciunt itaque! Nihil suscipit
        porro repudiandae officiis, exercitationem possimus expedita omnis, ut
        eveniet eos dolorum quas tenetur sint a distinctio facere delectus
        excepturi aliquam quaerat? Dignissimos hic exercitationem repellendus,
        possimus nemo, nesciunt accusantium eius dolorum a provident ducimus,
        corporis voluptate ipsum repudiandae obcaecati sed veniam necessitatibus
        voluptatum sit? Dolor, suscipit sint ad nisi ex consequatur omnis
        similique, saepe praesentium tempore a facilis assumenda voluptatem fuga
        neque. Ratione officia odio necessitatibus harum dolorem totam impedit?
        Aspernatur vero, assumenda iure numquam veritatis sequi, libero
        doloremque dolorem fugiat, officiis hic officia? Assumenda, delectus.
        Eligendi doloribus dolorum odio, expedita in debitis, vel illo enim sed
        voluptatibus sint exercitationem dignissimos consectetur quibusdam fugit
        provident ullam quo dolores quas asperiores repellat iste corporis,
        maxime harum. Corrupti labore nisi perferendis sunt reprehenderit nulla
        expedita, recusandae incidunt libero quibusdam facilis, odit placeat,
        harum iusto asperiores! Excepturi deleniti quod, iusto fugiat ad
        repudiandae labore neque commodi, sint eaque omnis quae nobis itaque ex!
        Earum, vel. Velit veniam porro sequi? Maxime quibusdam fugit ratione
        architecto praesentium sit fugiat, totam ducimus facilis? Tempore et
        laborum asperiores odio iusto ipsam dignissimos! Dolorum molestiae
        fugiat ipsa natus, impedit placeat neque eaque beatae inventore tenetur
        perferendis magni amet. Accusantium nisi, reprehenderit unde eveniet,
        fuga velit nesciunt eius, ea saepe suscipit illo. Sit, magni voluptates.
        Culpa, inventore excepturi! Esse quibusdam, non earum ea dolores
        consequatur inventore tempora quam sequi doloremque natus quaerat,
        mollitia voluptate eum soluta doloribus aspernatur praesentium amet!
        Itaque vitae dolorum eaque quibusdam vero recusandae expedita officia
        ipsam nulla! At corrupti dicta velit minus. Officiis architecto, odio
        facere quod obcaecati facilis. Sint quo reprehenderit expedita facere
        rem quaerat deserunt atque alias officia exercitationem, inventore
        molestias nisi veniam eveniet eligendi eius velit adipisci quam, harum
        obcaecati nesciunt animi doloremque debitis? Possimus, fugiat
        praesentium? Reiciendis blanditiis ea laudantium placeat molestias, nam
        quibusdam nihil aspernatur doloribus vel? Eos quod doloribus architecto
        consequuntur! Earum, commodi suscipit? Quis, sapiente! Dolor, in
        officiis inventore sequi pariatur repellat maiores ea ut doloremque
        totam minus! Aspernatur eum nam officia beatae impedit! Praesentium nisi
        laborum voluptatibus, quis eos ea quod id deleniti molestiae error ipsam
        porro sint sequi in aperiam saepe, molestias maiores ducimus sapiente
        suscipit incidunt aut? Nobis omnis neque ipsa, obcaecati distinctio ut,
        soluta odio laborum possimus quaerat delectus ab eius ipsum perferendis
        explicabo pariatur harum temporibus. Similique nemo neque sint. Corporis
        debitis voluptatibus nobis fugiat, tenetur accusantium porro fuga
        explicabo perferendis molestiae, ratione dolorem nesciunt vitae odio
        exercitationem. Molestias quos incidunt dignissimos consequuntur error.
        Unde, quidem? Velit sequi, fugiat pariatur quod dolorum, saepe possimus
        animi sit aut rerum vero itaque aspernatur? Incidunt tempore velit
        temporibus assumenda quas cumque libero dolores porro reprehenderit
        blanditiis nobis tenetur, deleniti exercitationem iure aliquam sunt quod
        suscipit minus quo officia, aspernatur voluptas, animi rerum!
      </ul>
    </div>
  </transition>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 1.9s ease;
}

.fade-enter-from {
  opacity: 0;
  scale: 0.5;
}
.fade-leave-to {
  opacity: 0;
  scale: 0;
}

.reviews-btn {
  border: 2px solid #ffd43b;
  padding: 15px;
  font-size: 18px;
  margin: 20px auto;
  border-radius: 10px;
  list-style: none;
  transition: all 0.3s ease-in;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  color: #ffd43b;
  text-decoration: none;
  &:hover {
  }
}

.reviews {
  position: absolute;
  padding: 15px;
  top: 96px;
  right: 0;
  bottom: 0;
  width: 30%;
  background: #d3d2d2;
  overflow-y: auto;
  z-index: 100;
}

li {
  width: 50%;

  border: 2px solid #ffd43b;
  padding: 15px;
  font-size: 18px;
  margin: 20px auto;
  border-radius: 10px;
  list-style: none;
  transition: all 0.3s ease-in;

  &:hover {
    transform: scale(1.1);
  }
}

ul {
  margin: 0;
  padding: 0;
}
</style>
